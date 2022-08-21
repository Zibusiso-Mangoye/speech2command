# listen for activation command
# playsound to alert user that activation command was accepted
# listen for audio input
# convert the audio to text 
# act on the command if its actionable or ask for clarification
from settings.load_config import load_config
from speech2command.core import S2CClient

def main(ACTIVATION_COMMAND: str)-> None:
    client = S2CClient()
    while True:
        a = client.get_audio()
        command = client.audio_to_text(a)

        if ACTIVATION_COMMAND in command.lower():
            print("activate")
            client.play_sound("What can I do for you?")

            note = client.get_audio()
            if note := client.audio_to_text(note):
                client.play_sound(note)

                # now = datetime.now().astimezone().isoformat()
                # res = client.create_page(note, now, status="Active")
                # if res.status_code == 200:
                #     play_sound("Stored new item")
                
                
if __name__ == "__main__":
    main(**load_config())
    