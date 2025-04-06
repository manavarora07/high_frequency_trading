import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from datetime import datetime, timedelta, timezone
import argparse
import time

def read_data(csv_file):
    try:
        df = pd.read_csv(csv_file)
        if df.empty or 'timestamp' not in df.columns:
            return pd.DataFrame()
        # Parse ISO8601 format like: 2025-04-06T05:42:31.374517+00:00
        df['timestamp'] = pd.to_datetime(df['timestamp'], format='ISO8601', utc=True)
        return df
    except Exception as e:
        print(f"[!] Error reading data: {e}")
        return pd.DataFrame()

def plot_trades(csv_file, rolling_window):
    print(f"\n[✓] Starting trade plotter with file: {csv_file}, rolling window: {rolling_window}\n")
    plt.ion()
    fig, ax = plt.subplots(figsize=(10, 6))

    while True:
        df = read_data(csv_file)

        print("\n=== RAW DATA (Tail) ===")
        print(df.tail())

        if rolling_window:
            cutoff = datetime.now(timezone.utc) - timedelta(seconds=rolling_window)
            print(f"\n[Info] Rolling window: last {rolling_window}s (Cutoff: {cutoff.isoformat()})")
            if 'timestamp' in df.columns:
                df = df[df["timestamp"] >= cutoff]

        print("\n=== FILTERED DATA (Tail) ===")
        print(df.tail())

        if not df.empty and 'timestamp' in df.columns:
            df['second'] = df['timestamp'].dt.floor('s')
            trades_per_second = df.groupby('second').size().rolling(window=5, min_periods=1).mean()


            ax.clear()
            ax.plot(trades_per_second.index, trades_per_second.values, color='cornflowerblue', label='Trades/s')

            ax.set_title(f"Trades per Second (last {rolling_window or 'all'}s)")
            ax.set_xlabel("Time")
            ax.set_ylabel("Trades per Second")
            ax.legend(loc="upper right")

            ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
            ax.xaxis.set_major_locator(mdates.AutoDateLocator())
            ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=20))

            fig.autofmt_xdate()
            plt.tight_layout()
        else:
            print("[!] No data to plot!")

        plt.pause(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Live Trade Plotter")
    parser.add_argument('--file', type=str, default='trade_log.csv', help="Path to CSV file (default: trade_log.csv)")
    parser.add_argument('--window', type=int, help="Rolling window in seconds (alias for --rolling)")
    parser.add_argument('--rolling', type=int, help="Rolling window in seconds (default: 600)")

    args = parser.parse_args()
    rolling_window = args.window if args.window is not None else (args.rolling or 600)

    plot_trades(csv_file=args.file, rolling_window=rolling_window)
