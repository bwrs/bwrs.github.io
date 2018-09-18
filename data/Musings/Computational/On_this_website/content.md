# Page sizes

The median desktop webpage, in this day and age, is a little over 1.5MB^[*The HTTP Archive*, accessed 2018-09-16.]; the median mobile page is 1.3MB.

## Is that big?

By historical standards, this is excessive. In 2010, the average page size was just half a megabyte. These days, the median mobile page is the same size as the compressed^[using standard algorithms] text of both the Bible and the Quran, and the desktop page is large enough to fit the Book of Mormon as well.

## Is that too big?

The majority of these sites are serving mostly text; such text probably doesn't exceed 10KB in the majority cases. Rather, the page is bulked by adverts, excessively high-resolution images, and superfluous use of entire Javascript libraries.

## Is this the raving of a lunatic?

Probably; but it is nevertheless of import. For a person like the author, on a humble mobile data package of 1GB each month, I am thus limited to about 26 webpages of median size per day; this is terribly inconvenient.

## This webpage

I indulge myself by forcing you to download a Google font in order to read this page properly; however, this font is only 200KB, so even when you download this, this webpage is 7 times smaller than the median.

However, this font is cached for a year; so excluding this yearly download, this webpage is not significantly worse than raw text^[although it uses `pandoc` to produce the HTML, which is perhaps sometimes excessively verbose.], and is at least 100 times smaller than the average webpage. At this size, on my 1GB monthly plan, I would be able to read at least three long^[i.e. containing a lot of content] pages per minute of my waking life.

## In the general case

For a smaller, and thus faster, webpage, it usually helps to avoid large JS libraries, and superfluous or large images. Ideally, adverts ought not to be used, as
 - they are designed to distract from the page
 - they increase file size and load times significantly
 - they are blocked anyway
 - Patreon &c. exist.

# Static webpages

These give better performance, security, &c.; this is well-documented. Website generators exist for this sort of thing; this webpage uses [an original^[modulo a reliance on `pandoc`] website generator](https://github.com/bwrs/bwrs.github.io).

# See also

 - [Joshua Loo's writings on his own webpage, which is laid out in a ridiculous fashion](https://joshualoo.net/#meta)
