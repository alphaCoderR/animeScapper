from halo import Halo

search_text = "Searching... Please Wait !!!"
search_loader = Halo(text=search_text, text_color="white",
                     color="magenta", spinner='dots', animation="marquee")

loading_text = "Loading.... Please Wait !!!"
loader = Halo(text=loading_text, text_color="white", spinner={
    'interval': 100,
    'frames': ["\\","|","/","-"]
}, color="magenta", animation="bounce")
