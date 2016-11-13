stream_url=https://sevenwestmedia01-i.akamaihd.net/hls/live/224814/SYD1/master_high.m3u8

while true
do
    date=`date +%Y-%m-%d`
    # 600 seconds (10 minute) duration to avoid errors causing hanging
    ffmpeg -t 600 -i "$stream_url" -vf fps=1/2 imgs/$date-img%d.png
done
