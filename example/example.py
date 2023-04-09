import vibe

if __name__ == "__main__":
    chart = vibe.ChartData()
    print(chart.name)
    print(chart.date)
    for entry in chart:
        print(entry)