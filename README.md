# GPT2

Right now, there is a simple Python script to generate a single (long) response to a couple of 
sentences.  This part seems to working well.  In the same script, there is code for a Conversation
mode, but that seemed to not work well at all, it kept truncating my responses to very few tokens
and generating very brief responses that didn't relate the question.  I'll see if I can tune the
code so that it is more useful.

This assumes that you have a functioning install of Huggingface's Transformers package installed 
and that it is working with Tensorflow.  For me, I used the latest version of Transformers (4.28.1),
and then I needed keras-nlp (current, 0.4.1), and these only worked with Tensorflow 2.10.  If you are 
using the tensorflow-metal package for Apple Silicon (M1/M2 processors), this needs to use version
0.6 to go with tensorflow-macos 2.10.

You will also need to download the gpt2 model using transformers, the gpt2-xl (largest available) model
was approx 6.2GB(!).  There are smaller versions (e.g. [GPT2-medium](https://huggingface.co/gpt2-medium), see 
'Related Models' section for others) that are less effective but smaller on your hard drive and faster.
