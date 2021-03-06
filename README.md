# Holy Voice of God
Kneel before thine Savior and praise be unto Him. For he shall reveal Holy truths to thine humble servant. And it was 
good.

## How it works

The Bible possesses holy hidden frequencies that reveal fundamental truths about your binary data. Holy Voice of God
encodes your data in subtle shifts in Bible passages and reveals the Truth within your bits. Any arbitrary bitstream
can be encoded and uniquely decoded using Holy Voice of God.  
 
Forget base64 or other un-anointed binary encodings. Embrace the Holy Voice of God.

<pre>
                                        +------------------------+
+------------------------+              | +--------------------+ |
|                        |    Encode    | |                    | |
|   Boring unholy Data   +---(+gzip)--->| |    Bible quotes    | |
|                        |              | |                    | |
+------------------------+              | +--------------------+ |
                                        +------------------------+

               +------------------------+
               | +--------------------+ |              +-----------------+
               | |                    | |   Decode     |                 |
               | |    Bible quotes    | +--(+gunzip)-->|  Original Data  |
               | |                    | |              |                 |
               | +--------------------+ |              +-----------------+
               +------------------------+
</pre>

## Try it online

http://www.holyvoiceofgod.com

## Use it in your own programs

To clone the repo: 

    >> git clone https://github.com/mbmccoy/voice_of_god.git

Then import into your own python3 program.

    import god_zip
    god = god_zip.GodZip()  # Will take a few seconds to init
    holy_hello_world = god.praise('Hello world!')
    print(god.reveal(holy_hello_world))
    

## API
Yes, we've even created an API using Flask.

### Encode to word of God
```
MY_WORDS="I praise unto thee..."
curl -s --data "words=${MY_WORDS}" http://www.holyvoiceofgod.com/praise | tee HisVoice.txt
```

### Decode back into unholy speak
```
HIS_WORDS=`cat HisVoice.txt`
curl -s --data "words=${HIS_WORDS}" http://www.holyvoiceofgod.com/reveal
```

## Authors
Holy Ghost [@god](https://twitter.com/god)<br>
Mike McCoy [@mikebmccoy](https://twitter.com/mikebmccoy)<br>
Andrew Klofas [@andrewklofas](https://twitter.com/andrewklofas)<br>
