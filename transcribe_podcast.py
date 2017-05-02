
import time
import pandas as pd

def main(): 

    transcriptions = {}
    ep_seconds = 4801
    chunk_seconds = 15

    for i in range(0, ep_seconds, chunk_seconds): 
        i_padded = '{:0>4}'.format(i)
        print(i_padded)
        transcriptions[i_padded] = transcribe_gcs('gs://roderick/to_clerd/rotl_0242_{}.flac'.format(i_padded))

    tsc = pd.Series(transcriptions, name='transcription')
    tsc.to_csv('transcription.csv', header=True)


def transcribe_gcs(gcs_uri):
    """Asynchronously transcribes the audio file specified by the gcs_uri."""

    from google.cloud import speech

    speech_client = speech.Client()

    audio_sample = speech_client.sample(
        content=None,
        source_uri=gcs_uri,
        encoding='FLAC'
        # sample_rate_hertz=16000
        )
    
    operation = audio_sample.long_running_recognize('en-US')

    retry_count = 100
    while retry_count > 0 and not operation.complete:
        retry_count -= 1
        time.sleep(2)
        operation.poll()
    
    if not operation.complete:
        print('Operation not complete and retry limit reached.')
        return

    alternatives = operation.results
    for alternative in alternatives:
        print('Transcript: {}'.format(alternative.transcript))
        print('Confidence: {}'.format(alternative.confidence))

    return alternative.transcript

    

if __name__ == '__main__': 
    main()