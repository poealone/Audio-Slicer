from pydub import AudioSegment
from pydub.export import wav
import os

def slice_audio(file_path, slice_duration):
    # Load the audio file
    audio = AudioSegment.from_file(file_path)

    # Get the duration of the audio in milliseconds
    audio_duration = len(audio)

    # Calculate the number of slices needed
    num_slices = audio_duration // slice_duration

    # Create a directory to store the sliced audio files
    output_dir = 'sliced_audio'
    os.makedirs(output_dir, exist_ok=True)

    # Slice the audio into segments
    for i in range(num_slices):
        # Calculate the start and end times for the slice
        start_time = i * slice_duration * 1000  # Convert to milliseconds
        end_time = (i + 1) * slice_duration * 1000

        # Extract the slice from the audio
        audio_slice = audio[start_time:end_time]

        # Save the slice as a new audio file
        slice_file_path = os.path.join(output_dir, f'slice{i}.wav')
        audio_slice.export(slice_file_path, format='wav')

        print(f'Slice {i} saved as {slice_file_path}')

    print('Slicing complete!')

# Example usage
file_path = 'path/to/your/audio/file.wav'
slice_duration = 10  # seconds

slice_audio(file_path, slice_duration)
