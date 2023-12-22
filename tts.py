import pyttsx3

engine = pyttsx3.init()

strs = "Man: How did it go?"\
+"Woman: I think it went quite well. I did a lot of research and prepared a lot. I was in there for ... I don't know ... half an hour?"\
+"Man: And? What did they say?"\
+"Woman: Nothing much. At the end I asked them, 'What happens now?', and the woman said, 'We'll call you back with news in three or four days.'"\
+"Man: Really?"\
+"Woman: Yeah, I think I've got the job. There weren't a lot of other people there. I was the only interview that day, you know?"\
+"Man: Well, good luck with it."

engine.say(strs)
# engine.save_to_file(strs, "audio.wav")
 
engine.runAndWait()