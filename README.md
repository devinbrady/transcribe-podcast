# transcribe-podcast
Use the Google Cloud Speech API to transcribe audio files from a podcast. 

## Background
"[Roderick on the Line](http://www.merlinmann.com/roderick/) is a frank and candid weekly phone call between John Roderick and Merlin Mann." 

The podcast has 244 episodes and about 20,000 minutes, so far. It consists of two men talking, with only minimal music and sound cues. 

For longtime fans, it can be difficult to remember which episode contained a particular discussion. There have been various efforts, such as a [wiki](http://roderickon.wikia.com/wiki/Roderick_on_the_Line_Wiki) and [index](http://wecancutthisout.com/), to document each episode. I thought, let's try to use "the clode" to transcribe it for us. 

This script should be general enough to transcribe any audio file. 

## Scripts
* `mp3_to_flac.sh`: bash script for converting one MP3 file to FLAC, in 15-second chunks. Run this first. 
	* Google Cloud Speech API prefers lossless audio codecs, though obviously converting from a lossy codec doesn't help us much here.
* `transcribe_podcast.py`: The main Python script for transcription. 

## To Do
* Run the script on a remote Google Cloud server rather than locally.
* Look for ways to speed up the transcription. 
* Try chunks longer than 15 seconds. 
* Explore using a model to split up John and Merlin's voices into separate audio files. 