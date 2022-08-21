# listen for activation command
# playsound to alert user that activation command was accepted
# listen for audio input
# convert the audio to text 
# act on the command if its actionable or ask for clarification
# each plugin has its own activation command or key word
#     check the list of available commands from the audio input

from settings.load_config import load_config
from speech2command.core import S2CClient

def main():
    client = S2CClient()
    audio_input = client.get_audio()
    command = client.audio_to_text(audio_input)
    print(command)
        
                
                
if __name__ == "__main__":
    main()
    