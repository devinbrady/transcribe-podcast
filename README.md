# transcribe-podcast
Use the Google Cloud Speech API to transcribe audio files from a podcast. 

## Background
[Roderick on the Line](http://www.merlinmann.com/roderick/) is a podcast hosted by John Roderick and Merlin Mann.

For longtime listeners, it can be difficult to remember which episode contained a particular discussion. There have been various efforts, such as a [wiki](http://roderickon.wikia.com/wiki/Roderick_on_the_Line_Wiki) and [index](http://wecancutthisout.com/), to document each episode. I thought, let's try to use "the clode" to transcribe it for us. 

The podcast has 244 episodes and about 20,000 minutes, so far. It consists of two men talking, with only minimal music and sound cues. 

The transcript doesn't have to be perfect, as long as it captures some key words. That would allow fans to search the text and jump to the audio where that word appears. 

This script should be general enough to transcribe any audio file. 

## Example
From minute 2 of [Episode 242](http://www.merlinmann.com/roderick/ep-242-mr-jingle-jangle.html): 

| Start Time (s)  | Confidence  | Transcript  |
|---|---|---|
|  0060 | 0.879  | is that a bugger feature well here's the thing a long story short I'm pretty sure it's probably the power supply for a variety of reasons including that it takes about 5 days to get an appointment I've been doing  |
| 0075  | 0.780  | crazy monkey trying to like figure if I can troubleshoot of myself I think I've tried everything I reset mini mini things  |
| 0090  | 0.929  | peers so far that your computer guy well I used to be sure it appears that if I don't as long as I don't use a certain keyboard it stays up for at least 36 hours I just I love our relationship  |
| 0105  | 0.782  | I get the stronger lationship but if for some reason I suddenly stop talking because I understand pretty  |


## Scripts
* `mp3_to_flac.sh`: bash script for converting one MP3 file to FLAC, in 15-second chunks. Run this first. 
	* Google Cloud Speech API prefers lossless audio codecs, though obviously converting from a lossy codec doesn't help us much here.
* `transcribe_podcast.py`: The main Python script for transcription. 

## To Do
* Run the script on a remote Google Cloud server rather than locally.
* Look for ways to speed up the transcription. 
* Try chunks longer than 15 seconds. 
* Explore using a model to split up John and Merlin's voices into separate audio files. 