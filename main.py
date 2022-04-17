from flask import Flask, render_template, request, redirect
import scrapeurl, comparator
import nltk
nltk.download('punkt')
nltk.download('stopwords')
#on startup install news-fetch, nltk download punkt, stopwords
app = Flask('app')
app.config["TEMPLATES_AUTO_RELOAD"] = True

# pretty sure these still aren't global and therefore aren't serving any purpose being here
url1 = ''
url2 = ''
scraped_urls = ''
tops = ''
keywords = ''

@app.route('/', methods=["GET", "POST"])
def index():    
    if request.method == "POST":
        url1 = request.form.get("url1","")
        url2 = request.form.get("url2","")

        if not url1:
            url1 = "https://www.reuters.com/world/europe/how-big-loss-russia-is-sinking-moskva-missile-cruiser-2022-04-15/"
        if not url2:
            url2 = "https://www.rt.com/russia/553902-flagship-sank/"
        
        # scrapes each url, returning dictionaries
        global scraped_urls
        scraped_urls = scrapeurl.scrape_urls(url1, url2)
        # keywords are collected from each article, then the keywords common to both are stored    
        #if scraped_urls == "Error", goes to error page
        if scraped_urls == "Error":
            return render_template("error.html")

        global keywords
        keywords = [*{*scraped_urls[0]["keyword"]} & {*scraped_urls[1]["keyword"]}]

        # runs comparator to identify commonalities
        analysis = comparator.make_structure()
        global tops
        tops = comparator.read_structure(analysis)
        
        return redirect("/final")

    else:
        return render_template("index.html")

@app.route('/final', methods=["GET", "POST"])
def final():
    if request.method == "POST":
        print(request.form.get("keyword"))
        word = request.form.get("keyword")
        return render_template("final.html", keywords = keywords, scraped_urls = 

    scraped_urls, tops = tops, word=word, prtop = tops[word]['closest'], lowtop = tops[word]['furthest'])

    else:
        word=keywords[0]
        return render_template("final.html", keywords = keywords, scraped_urls = scraped_urls, tops = tops, word=word, prtop = tops[word]['closest'], lowtop = tops[word]['furthest'])
        
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)