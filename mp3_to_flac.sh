
# echo $BASH_VERSION

# This script converts an MP3 file to FLAC in 15-second chunks

ep="rotl_0242"

for start_time in {0..4800..15}
do
    echo "$start_time"
    printf -v zero_pad_start "%04d" $start_time
    ffmpeg -ss "$start_time" -t 15 -i "episodes/$ep.mp3" to_clerd/"$ep"_"$zero_pad_start".flac
done


