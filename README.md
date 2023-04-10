# 💓 바이브 차트 API: vibe-chart.py
![vibe](./image.png)

vibe-chart.py is a Python API that retrieves the TOP 100 information from the [Naver Vibe](https://vibe.naver.com/).

## Installation
```commandline
pip install vibe-chart.py
```

## Quickstart
The main usage of vibe-chart.py is similar to [billboard.py](https://github.com/guoguo12/billboard-charts).
```commandline
>>> from vibe import *
>>> chart = ChartData(image_size=500)
>>> print(chart[0].json())
{
    "artist": "IVE(아이브)",
    "image": "https://musicmeta-phinf.pstatic.net/album/009/334/9334427.jpg?type=r500Fll&v=20230404132130",
    "isNew": false,
    "lastPos": 1,
    "rank": 1,
    "title": "Kitsch"
}
>>> print(chart.name)
오늘 Top 100
>>> print(chart.date)
2023-04-09 07:00:00
```

### ChartData Arguments
- `name` – The chart name
- `date` – The chart date
- `queryStart` – The starting index of the chart entries to be retrieved from the Vibe API. (default: 1)
- `queryCount` – The number of items to retrieve from the API response, starting from `queryStart`. (default: 100)
- `imageSize` – The size of cover image for the track. (default: 256)
- `fetch` – A boolean value that indicates whether to retrieve the chart data immediately. If set to `False`, you can fetch the data later using the `fetchEntries()` method.

### Chart entry attributes
`ChartEntry` can be accessed using the `ChartData[index]` syntax. A `ChartEntry` instance has the following attributes:
- `title` – The title of the track
- `artist` – The name of the artist
- `image` – The URL of the cover image for the track
- `lastPos` - The track's last position on the previous period.
- `rank` – The track's current rank position on the chart.
- `isNew` – Whether the track is new to the chart.

### K-Pop music chart Python APIs
- [Melon | melon-chart.py](https://github.com/gold24park/melon-chart.py)
- [Bugs | bugs-chart.py](https://github.com/gold24park/bugs-chart.py)
- [Genie | genie-chart.py](https://github.com/gold24park/genie-chart.py)
- [Vibe | vibe-chart.py](https://github.com/gold24park/vibe-chart.py)
- [Flo | flo-chart.py](https://github.com/gold24park/flo-chart.py)

## Dependencies
- [requests](https://requests.readthedocs.io/en/latest/)

## License
This project is licensed under the MIT License.
