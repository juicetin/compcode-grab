stream_url=https://sevenwestmedia01-i.akamaihd.net/hls/live/224814/SYD1/master_high.m3u8
date=`date +%Y-%m-%d`
# ffmpeg -i "$stream_url" -c copy "$output_file"
ffmpeg -i "$stream_url" -vf fps=1/2 imgs/$date-img%d.png
