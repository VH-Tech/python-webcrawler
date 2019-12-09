<h1>Ways to prevent web scraping:</h1>

<b>.1. Require a login for access:</b>
    So bots cant download your websites html anonymously.

<b>2. change your websites html regularly</b>
    By changing your websites pattern regularly you make it less vulnerable to web scrapers.

<b>3. using CAPTCHAs</b>
    To protect access of bots to your website.

<b>4. Don't expose your complete dataset</b>
    The lesser you expose your data lesser the information attacker gets.
    
<b>5. Don't accept requests if the User Agent is empty / missing.</b>
    Sometimes attackers forget to mention user headers with their bots.
    
<b>6. Use and require cookies; use them to track user and scraper actions.</b>
<b>7. Use JavaScript + Ajax to load your content</b>
    This will make the content inaccessible to HTML parsers which do not run JavaScript. This is often an effective
    deterrent to newbie and inexperienced programmers writing scrapers.
