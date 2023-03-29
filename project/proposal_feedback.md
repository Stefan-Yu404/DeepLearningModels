### Proposal feedback

6/10

This is a good start, but there are some details missing; please answer the following questions for full points.

This isn’t a question, but regarding your concern and essential goal #2: it probably makes sense to start by scaling, resizing, and/or cropping the images so that you can give images a consistent size to your model. There are various existing implementations of this kind of preprocessing which you should be able to draw from. 

Essential goal #1 and Desired goal #1: Where is the data from other painters? Do you have another dataset in mind? 

Desired goal #2: this is much more difficult than the task of just learning to generate images that look similar to those in your Munch dataset. This task requires training your model to “disentangle” the painter’s style from the specific content so that you can change the style without changing other aspects of the drawing. The GAN you described in the proposal doesn’t indicate how that would be possible. Do you have a sense of how you hope to train a model to do this? How will you evaluate whether it works?
