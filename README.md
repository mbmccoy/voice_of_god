# Holy Voice of God
Kneel before thine Savior and praise be unto Him. For he shall reveal Holy truths to thine humble servant. And it was good.

## How it works
Using the Bible, we analysed the frequency of words and their groupings and created a unique mapping (sort of like a fingerprint). From this, we can encode any data into random phrases that closely resemble passages from the Bible, and decode them back into the original data.

<pre>
+----------+             +---------------------+             +-----------------+
|          |   Encode    |                     |   Decode    |                 |
|   Data   +------------>|  Bible-like quotes  +------------>|  Original Data  |
|          |             |                     |             |                 |
+----------+             +---------------------+             +-----------------+
</pre>

## Try it
http://www.holywordofgod.com

## API
Yes, we've even created an API.

### Encode to word of God
```
curl --data "words=I praise unto thee" http://www.holywordofgod.com/praise
```

### Decode back into unholy speak
```
curl --data "words=Thine Holy response as sent from above" http://www.holywordofgod.com/reveal
```

## Authors
Holy Ghost<br>
Mike McCoy<br>
Andrew Klofas<br>
