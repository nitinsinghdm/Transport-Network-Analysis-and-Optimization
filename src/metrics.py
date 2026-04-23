def format_time(td):
    total_seconds = int(td.total_seconds())
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return f"{minutes} Min {seconds} Sec"

def summarize_times(series):
    stats = series.describe()

    return {
        "count": int(stats["count"]),
        "mean": stats["mean"],
        "min": stats["min"],
        "25%": stats["25%"],
        "50%": stats["50%"],
        "75%": stats["75%"],
        "max": stats["max"]
    }

def to_minutes(td_series):
    return td_series.dt.total_seconds() / 60