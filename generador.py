from google import genai

# Pega tu API Key aquí
genai.configure(api_key="TU_API_KEY")

client = genai.Client()

prompt = "Un paisaje futurista al atardecer, drones volando, estilo cinemático."

video = client.models.generate_videos(
    model="veo-3.1",
    prompt=prompt
)

with open("video_generado.mp4", "wb") as f:
    f.write(video.result())

print("Video generado: video_generado.mp4")
