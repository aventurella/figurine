# Figurine

**Simple, structure only models with inheritance**

Figurine is intended for dumb models. In other words, data only, no methods.
For web apps, view models come to mind, or anywhere you would like a model that
does nothing but represent data. 

### What about namedtuples?
Yes, you could just use namedtuple for this, and that might even be better.
If you want your model defs to look more like traditional python objects however,
Figurine can help.

It still may be that namedtuples are a better solution, though you may 
need a factory function to start them off with defaults of your choosing.

The base of a figuerine object is a dict, which is a bit better, for my need, for 
JSON serialization if needed.
