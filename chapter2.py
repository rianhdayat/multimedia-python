from PIL import Image

# Memuat gambar
image = Image.open('rian.jpg')

# Menyimpan gambar
image.save('hidayat.jpg')

cropped_image = image.crop((10, 10, 200, 200))
cropped_image.save('crop.jpg')

resized_image = cropped_image.resize((100, 100))
resized_image.save('resize.jpg')

from PIL import ImageFilter

filtered_image = resized_image.filter(ImageFilter.BLUR)
filtered_image.save('filtered.jpg')

from pydub import AudioSegment

# Memuat file audio
audio = AudioSegment.from_file('Al mulk 30s.mp3')

# Menyimpan file audio
audio.export('result.mp3', format='mp3')

clipped_audio = audio[:10000]  # Mendapatkan 10 detik pertama
clipped_audio.export('clip.mp3', format='mp3')

combined_audio = audio + clipped_audio
combined_audio.export('combine.mp3', format='mp3')

audio.export('combine.wav', format='wav')

louder_audio = audio + 10  # Meningkatkan volume sebesar 10dB
louder_audio.export('louder.mp3', format='mp3')