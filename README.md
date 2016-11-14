# Competition Code Grabber

Little utility to grab daily competition codes from TV streaming websites. Basically what it does is grab the streaming links from TV sites, uses ffmpeg to do image captures of them at short intervals, and detect when codeword screenshots pop up, and process them/extract the word from the image, and email it.

Currently only doing channel 7, as the encrypted stream links are directly available. Channel 9 requires both login and Flash, but will look into it at a later date.

Available functionality:
* Filter the collected images to only keep valid images (otherwise there'll be thousands a day
* Identify the actual text in the relevant images
* Email the codeword for each day

Future (maybe) functionality:
* Automatically text the codeword each day (not sure if able to programmatically text to 19XX- numbers)
