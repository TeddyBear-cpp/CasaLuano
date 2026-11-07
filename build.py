from pathlib import Path
from html import escape

ROOT = Path(__file__).parent / "dist"
SITE_URL = "https://teddybear-cpp.github.io/CasaLuano/"
SHARE_IMAGE_URL = SITE_URL + "assets/share-preview.jpg"

ARROW = '''<svg class="arrow-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 12h15m-6-6 6 6-6 6"/></svg>'''
FLOWER = '''<svg class="brand-flower" viewBox="0 0 80 80" fill="none" aria-hidden="true"><g stroke="currentColor" stroke-width="2.2" stroke-linecap="round">''' + ''.join(f'<ellipse cx="40" cy="17" rx="5.5" ry="13" transform="rotate({i*30} 40 40)"/>' for i in range(12)) + '''<circle cx="40" cy="40" r="12" fill="currentColor"/><path d="M39 51c3 10 2 18 0 27M40 66c-10-1-15-6-17-12 9 0 14 4 17 12Zm0 5c8-7 13-7 18-7-4 6-10 9-18 7Z"/></g></svg>'''
LARGE_FLOWER = FLOWER.replace('class="brand-flower"', 'class="hero-sun"')
MINI_FLOWER = FLOWER.replace('class="brand-flower"', 'class="flower-mini"')


def button(text, href, style="sun", external=False):
    extra = ' target="_blank" rel="noopener noreferrer"' if external else ''
    return f'<a class="button button-{style}" href="{href}"{extra}>{text} [[ARROW]]</a>'


def header(current):
    links = [
        ("paint", "Paint pottery", "paint.html"),
        ("wheel", "The wheel", "wheel.html"),
        ("menu", "Food & drink", "menu.html"),
        ("gather", "Gather", "gather.html"),
        ("visit", "Visit", "visit.html"),
    ]
    nav = ''.join(f'<a href="{href}"{(" aria-current=\"page\"" if current == key else "")}>{label}</a>' for key, label, href in links)
    return f'''<a class="skip-link" href="#content">Skip to content</a>
<header class="site-header"><div class="header-inner">
  <a class="brand" href="index.html" aria-label="Casa Luano home">[[FLOWER]]<span class="brand-type">Casa Luano<small>by Wildflower</small></span></a>
  <nav class="nav-links" id="primary-navigation" aria-label="Main navigation">{nav}</nav>
  <div class="header-actions">{button('Plan a visit', 'visit.html', 'dark')}<button class="menu-toggle" type="button" aria-label="Open navigation" aria-controls="primary-navigation" aria-expanded="false"><span></span></button></div>
</div></header>'''


def footer():
    return f'''<footer class="site-footer"><div class="container">
  <div class="footer-top"><div><span class="eyebrow">See you soon</span><h2>Make room for<br><span class="serif">a little mess.</span></h2>{button('Plan a visit', 'visit.html', 'sun')}</div><img class="footer-logo" src="assets/casa-luano-logo.png" alt="Casa Luano sunflower logo" loading="lazy"></div>
  <div class="footer-bottom">
    <div><h3>Casa Luano by Wildflower</h3><p>Clay, food and good company in Olympia, Lusaka.</p></div>
    <div><h3>Explore</h3><a href="paint.html">Pottery painting</a><a href="wheel.html">Wheel workshops</a><a href="menu.html">Food & drink</a><a href="gather.html">Group visits</a></div>
    <div><h3>Find us</h3><a href="visit.html">Visit Casa Luano</a><a href="https://www.instagram.com/casaluano/" target="_blank" rel="noopener noreferrer">Instagram ↗</a><a href="https://www.google.com/maps/search/?api=1&query=Casa+Luano+Olympia+Lusaka" target="_blank" rel="noopener noreferrer">Directions ↗</a></div>
  </div>
  <div class="footer-legal"><span>© Casa Luano concept preview</span><span>Independent design concept. Details to confirm with the café.</span></div>
</div></footer>'''


def wheel_section(title="Give the wheel a whirl.", copy="Scroll past it or drag it yourself. A little preview of the satisfying rhythm of clay on the wheel.", action="Explore wheel workshops", href="wheel.html"):
    return f'''<section class="wheel-section section"><div class="container wheel-grid"><div class="wheel-copy reveal"><span class="eyebrow">A little play before you visit</span><h2>{title.replace('whirl.', '<span class="serif">whirl.</span>')}</h2><p>{copy}</p>{button(action, href, 'sun')}</div><div class="wheel-art reveal reveal-delay-1"><div class="wheel-rotor" data-pottery-wheel role="slider" tabindex="0" aria-label="Spin the pottery wheel" aria-valuemin="0" aria-valuemax="359" aria-valuenow="0" aria-valuetext="Turned 0 degrees"><div class="wheel-vessel"><span class="wheel-finger-mark"></span></div></div><span class="wheel-instruction">drag me, or scroll on by</span></div></div></section>'''


def info_band(title, copy, action, href="https://www.instagram.com/casaluano/"):
    return f'''<section class="info-band"><div class="container info-band-grid"><div><span class="eyebrow">Make a plan</span><h2>{title}</h2></div><p>{copy}</p>{button(action, href, 'dark', href.startswith('https://'))}</div></section>'''


def base(page, title, description, body):
    page_url = SITE_URL if page == "home" else SITE_URL + page + ".html"
    share_title = "Casa Luano — A little clay, a lot of joy" if page == "home" else f"{title} · Casa Luano"
    share_description = ("An independent website concept showing pottery painting, wheel workshops, food and good company at Casa Luano in Lusaka."
                         if page == "home" else f"{description} Independent concept preview.")
    html = f'''<!doctype html><html lang="en" class="js"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#f8f3e9"><meta name="robots" content="noindex">
<meta name="description" content="{escape(description, quote=True)}"><title>{escape(title)} · Casa Luano</title>
<link rel="canonical" href="{page_url}">
<meta property="og:type" content="website"><meta property="og:site_name" content="Casa Luano by Wildflower">
<meta property="og:url" content="{page_url}"><meta property="og:title" content="{escape(share_title, quote=True)}">
<meta property="og:description" content="{escape(share_description, quote=True)}">
<meta property="og:image" content="{SHARE_IMAGE_URL}"><meta property="og:image:type" content="image/jpeg">
<meta property="og:image:width" content="1440"><meta property="og:image:height" content="960">
<meta property="og:image:alt" content="Handmade black and white checkerboard ceramic tea set against a bright green backdrop">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{escape(share_title, quote=True)}">
<meta name="twitter:description" content="{escape(share_description, quote=True)}"><meta name="twitter:image" content="{SHARE_IMAGE_URL}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="icon" href="favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="styles.css"><script src="site.js" defer></script>
</head><body>{header(page)}<main id="content">{body}</main>{footer()}</body></html>'''
    return html.replace('[[ARROW]]', ARROW).replace('[[FLOWER]]', FLOWER).replace('[[LARGE_FLOWER]]', LARGE_FLOWER).replace('[[MINI_FLOWER]]', MINI_FLOWER)


home = f'''
<section class="home-hero"><div class="container hero-grid">
  <div class="hero-copy reveal"><span class="eyebrow">Lusaka's clay café</span><h1><span>Make</span><span class="serif">something</span><span>wonderful.</span></h1><p>Pick up a brush, try the wheel, order something lovely and stay a little longer. At Casa Luano, getting your hands messy is part of the magic.</p><div class="hero-actions">{button('Find your thing', '#experiences', 'dark')}{button('See the menu', 'menu.html', 'outline')}</div></div>
  <div class="hero-side reveal reveal-delay-1">[[LARGE_FLOWER]]<svg class="hero-scribble" viewBox="0 0 280 130" fill="none" aria-hidden="true"><path d="M9 102C59 5 109 114 176 42c37-40 62-33 95-18" stroke="currentColor" stroke-width="8" stroke-linecap="round"/></svg><div class="film-wrap"><div class="film-frame"><video data-autoplay-video muted playsinline loop preload="metadata" poster="assets/painted-bowls.jpg" aria-label="Visitors at Casa Luano making and painting pottery"><source src="assets/clay-date.mp4" type="video/mp4"></video><button class="video-control is-paused" type="button" aria-label="Play video" aria-pressed="false"><svg class="pause-shape" viewBox="0 0 24 24" aria-hidden="true"><rect x="5" y="3" width="5" height="18"/><rect x="14" y="3" width="5" height="18"/></svg><svg class="play-shape" viewBox="0 0 24 24" aria-hidden="true"><path d="m7 3 15 9-15 9z"/></svg></button></div><span class="film-label">Come clay<br>with us!</span></div></div>
</div><span class="hero-bottom-note">Scroll to explore the café ↓</span></section>
<div class="word-ribbon" aria-label="Paint, throw, eat, stay a while"><div class="container"><span>Paint a piece</span><i></i><span>Throw some clay</span><i></i><span>Eat something good</span><i></i><span>Stay a while</span></div></div>
<section class="section"><div class="container intro-grid"><div class="reveal"><span class="eyebrow">A different kind of afternoon</span><h2>Come as you are.<br><span class="serif">Leave with a story.</span></h2><p>Casa Luano brings pottery painting, wheel throwing and a cosy café together in one colourful space. Come on your own, bring a friend, make something imperfect and make a day of it.</p>{button('The story behind Casa Luano', 'visit.html', 'outline')}</div><div class="intro-visual"><svg class="paint-ring" viewBox="0 0 250 230" fill="none" aria-hidden="true"><path d="M214 49C184 4 99 2 48 37-17 82 1 167 57 198c57 31 139 19 170-43" stroke="currentColor" stroke-width="9" stroke-linecap="round"/></svg><img src="assets/checker-tea-set.jpg" alt="Handmade black and white checkerboard teapot and cups" loading="lazy"><span class="hand hand-note">made by hand,<br>made to keep</span></div></div></section>
<section class="section experiences" id="experiences"><div class="container"><div class="section-heading reveal"><div><span class="eyebrow">Pick your kind of play</span><h2>There’s more than<br><span class="serif">one way to make.</span></h2></div><p>From your first brushstroke to the first pull on the wheel, there’s a place for you here.</p></div><div class="experience-grid">
  <a class="experience-card reveal" href="paint.html"><img src="assets/painted-bowls.jpg" alt="Colourful hand-painted ceramic bowls" loading="lazy"><div class="experience-content"><div><span class="eyebrow">01 · Take a seat</span><h3>Paint pottery</h3><p>Choose a handmade piece, then make it completely yours.</p></div><span class="circle-arrow">[[ARROW]]</span></div></a>
  <a class="experience-card reveal reveal-delay-1" href="wheel.html"><img src="assets/handmade-cup.jpg" alt="A handmade textured clay cup held in a potter's hand" loading="lazy"><div class="experience-content"><div><span class="eyebrow">02 · Get stuck in</span><h3>Try the wheel</h3><p>Centre, shape and pull your first little vessel.</p></div><span class="circle-arrow">[[ARROW]]</span></div></a>
  <a class="experience-card reveal" href="menu.html"><img src="assets/checker-teapot-detail.jpg" alt="Close-up of a handmade ceramic teapot" loading="lazy"><div class="experience-content"><div><span class="eyebrow">03 · Stay for more</span><h3>Eat & sip</h3><p>Breakfast, light bites, hearty plates and something to drink.</p></div><span class="circle-arrow">[[ARROW]]</span></div></a>
</div></div></section>
{wheel_section()}
<section class="section gallery-section"><div class="container"><div class="section-heading reveal"><div><span class="eyebrow">Objects with personality</span><h2>A little look at<br><span class="serif">what's possible.</span></h2></div><p>Every piece starts as clay. The rest is yours to imagine.</p></div><div class="gallery-grid"><figure class="reveal"><img src="assets/frog-incense.jpg" alt="Handmade frog incense holder with a pink flower" loading="lazy"><figcaption>The little characters</figcaption></figure><figure class="reveal reveal-delay-1"><img src="assets/painted-planter.jpg" alt="Painted geometric ceramic planter" loading="lazy"><figcaption>The colourful corners</figcaption></figure><figure class="reveal reveal-delay-2"><img src="assets/buddha-planter.jpg" alt="Handmade planter with a seated figure and succulents" loading="lazy"><figcaption>The one-of-a-kinds</figcaption></figure></div><div class="gallery-note">{button('Explore pottery painting', 'paint.html', 'outline')}</div></div></section>
<section class="section menu-teaser"><div class="container menu-teaser-grid"><div class="reveal"><span class="eyebrow">A table to come back to</span><h2>Paint, sip,<br><span class="serif">stay for dinner.</span></h2><p>A good afternoon deserves a good plate. Find breakfast, snacks, grill favourites, coffee, cocktails and more on the café menu.</p>{button('Browse food & drink', 'menu.html', 'dark')}</div><div class="menu-paper reveal reveal-delay-1"><span class="hand">one more bite?</span><h3>A few favourites</h3><div class="menu-row"><strong>Breakfast sandwich</strong><span>K180</span></div><div class="menu-row"><strong>Casa BBQ wings</strong><span>K140</span></div><div class="menu-row"><strong>Classic margherita pizza</strong><span>K160</span></div><div class="menu-row"><strong>Luano ginger honey tea</strong><span>K70</span></div><div class="menu-row"><strong>Homemade lemonade</strong><span>K60</span></div></div></div></section>
<section class="section visit-teaser"><div class="container visit-teaser-grid"><div class="visit-teaser-photo reveal"><img src="assets/planters-collection.jpg" alt="A collection of colourful ceramic planters on wooden stands" loading="lazy">[[MINI_FLOWER]]</div><div class="reveal"><span class="eyebrow">Find us in Olympia</span><h2>Your next favourite<br><span class="serif">afternoon is here.</span></h2><p>Come for a quick coffee or make a whole day of painting, making and catching up. We’ll save a little space at the table.</p>{button('Plan your visit', 'visit.html', 'dark')}</div></div></section>
'''


paint = f'''
<section class="page-hero paint-hero"><div class="container"><div class="reveal"><span class="eyebrow">Pottery painting · at Casa Luano</span><h1>A little paint.<br><span class="serif">A lot of you.</span></h1><p>Choose a handmade piece from Wildflower Ceramics, settle in with a drink, and let your imagination take the lead.</p>{button('How it works', '#how-it-works', 'dark')}</div><div class="page-hero-photo reveal reveal-delay-1"><img src="assets/painted-bowls.jpg" alt="Painted ceramic bowls in rose, blue, green and lilac" fetchpriority="high"><span class="corner-note">colour outside the lines</span></div></div></section>
<section class="section" id="how-it-works"><div class="container chapter-grid"><div class="reveal"><span class="chapter-label">01 / The experience</span><h2>Pick it.<br>Paint it.<br><span class="serif">Keep it.</span></h2></div><div class="reveal reveal-delay-1"><p class="chapter-lead">No perfect lines required. Just a piece you love, a palette of colour and time to make something that feels like you.</p><ol class="steps"><li><span class="step-number">01</span><div><h3>Choose your piece</h3><p>Browse the Wildflower shelves for a mug, bowl, plate or a little treasure. Each one is handmade.</p></div></li><li><span class="step-number">02</span><div><h3>Make your palette</h3><p>Find a spot at Casa Luano, order something to sip or snack on, and paint away.</p></div></li><li><span class="step-number">03</span><div><h3>Leave the kiln to us</h3><p>Wildflower Ceramics takes care of glazing and firing after your painting session.</p></div></li><li><span class="step-number">04</span><div><h3>Collect your creation</h3><p>Come back for your finished piece when it's ready, usually within two to four weeks.</p></div></li></ol></div></div></section>
<section class="split-feature"><div class="feature-image"><img src="assets/checker-tea-set.jpg" alt="Black and white checkerboard ceramic tea set" loading="lazy"></div><div class="feature-copy"><span class="eyebrow">The good part</span><h2>All the colour.<br>Kiln work included.</h2><p>Pottery painting ranges from K150 to K800 depending on the piece. Paints, glazing and firing are included.</p><p>Walk-ins are welcome during café opening hours. For a special occasion or a group, please enquire in advance.</p>{button('Make it a group day', 'gather.html', 'light')}</div></section>
<section class="section gallery-section"><div class="container"><div class="section-heading reveal"><div><span class="eyebrow">A shelf full of ideas</span><h2>Find your<br><span class="serif">starting point.</span></h2></div><p>Little things, useful things, statement pieces. Every piece leaves room for your own imagination.</p></div><div class="simple-gallery"><figure class="reveal"><img src="assets/checker-teapot-detail.jpg" alt="Checkerboard teapot detail" loading="lazy"><figcaption>Mugs & tea things</figcaption></figure><figure class="reveal reveal-delay-1"><img src="assets/cactus-planter.jpg" alt="Cactus in a decorated ceramic planter" loading="lazy"><figcaption>Planters</figcaption></figure><figure class="reveal"><img src="assets/frog-detail.jpg" alt="Handmade frog incense holder" loading="lazy"><figcaption>Little characters</figcaption></figure><figure class="reveal reveal-delay-1"><img src="assets/buddha-detail.jpg" alt="Handmade sculptural planter detail" loading="lazy"><figcaption>Statement pieces</figcaption></figure></div></div></section>
{info_band('Ready to paint your own?', 'Drop by during café hours, or enquire ahead for a group or special occasion.', 'Find us on Instagram')}
'''


wheel = f'''
<section class="page-hero wheel-hero"><div class="container"><div class="reveal"><span class="eyebrow">Wheel throwing · hosted by Wildflower Ceramics</span><h1>Feel the clay<br><span class="serif">come alive.</span></h1><p>In a guided 90-minute session, learn to centre, shape and pull the walls of clay to make your first vessel.</p>{button('Explore sessions', '#sessions', 'dark')}</div><div class="page-hero-photo reveal reveal-delay-1"><img src="assets/handmade-cup.jpg" alt="Close-up of a handmade textured clay cup" fetchpriority="high"><span class="corner-note">come clay with us</span></div></div></section>
{wheel_section('Give the wheel a whirl.', 'The best way to understand the rhythm is to feel it. Drag this little wheel or scroll by to set it turning. Then come try the real thing at Casa Luano.', 'See session options', '#sessions')}
<section class="section" id="sessions"><div class="container"><div class="section-heading reveal"><div><span class="eyebrow">Find your flow</span><h2>One spin or<br><span class="serif">a whole new hobby.</span></h2></div><p>Both options are guided by an instructor and include clay, tools and firing.</p></div><div class="price-panel"><article class="price-card reveal"><span class="eyebrow">Wheel throwing 101</span><div class="price">K800 <small>/ person</small></div><h3>Single wheel experience</h3><p>One 90-minute guided session to make your first vessel.</p><ul><li>K750 per person for groups of 3 or more</li><li>Clay, tools and firing included</li><li>Return to paint or glaze for K200 per item</li></ul></article><article class="price-card is-featured reveal reveal-delay-1"><span class="eyebrow">More time to make</span><div class="price">K2,700 <small>/ person</small></div><h3>The wheel deal</h3><p>Four 90-minute sessions across any four days within a month.</p><ul><li>Make up to four items</li><li>Glazing of one piece included</li><li>Additional pieces can be painted or glazed</li></ul></article></div><p class="price-note">Prices may change; please confirm when booking.</p></div></section>
<section class="split-feature clay-feature"><div class="feature-image"><img src="assets/painted-bowls.jpg" alt="A group of painted handmade ceramic bowls" loading="lazy"></div><div class="feature-copy"><span class="eyebrow">From wet clay to keepsake</span><h2>Your hands make<br>the first move.</h2><p>The instructor guides you the whole way. The clay might wobble; that’s part of learning. Your finished piece is fired, and you can return to add colour to it.</p>{button('See pottery painting', 'paint.html', 'light')}</div></section>
<section class="section"><div class="container"><div class="section-heading reveal"><div><span class="eyebrow">Good to know</span><h2>First time?<br><span class="serif">You belong here.</span></h2></div></div><div class="faq-list"><details class="reveal"><summary>Do I need to know how to use the wheel?</summary><p>No. Wheel throwing 101 is an introductory session with an instructor to guide you through the process.</p></details><details class="reveal"><summary>What is included?</summary><p>The session includes the instructor, clay, tools and firing.</p></details><details class="reveal"><summary>Can I add colour to my piece?</summary><p>Yes. Return to paint or glaze your piece for an additional K200 per item. Confirm the current price when booking.</p></details><details class="reveal"><summary>Can I bring friends?</summary><p>Yes. The listed group rate is K750 per person for three or more people.</p></details></div></div></section>
{info_band('Your first spin awaits.', 'Ask Casa Luano about session availability before you come.', 'Find us on Instagram')}
'''


def menu_item(name, description, price):
    return f'<article class="menu-item"><div><h3>{name}</h3><p>{description}</p></div><span class="item-price">{price}</span></article>'


def menu_group(group_id, title, intro, items):
    return f'''<section class="menu-group" id="{group_id}"><div class="container"><div class="menu-group-head reveal"><h2>{title}</h2><p>{intro}</p></div><div class="menu-list reveal">{''.join(menu_item(*item) for item in items)}</div></div></section>'''


menu = f'''
<section class="page-hero menu-hero"><div class="container"><div class="reveal"><span class="eyebrow">The café table</span><h1>Stay for<br><span class="serif">one more bite.</span></h1><p>A menu made for long chats, paint-covered hands and whichever part of the day you’re in.</p>{button('Explore the menu', '#menu-intro', 'dark')}</div><div class="page-hero-photo reveal reveal-delay-1"><img src="assets/checker-tea-set.jpg" alt="Handmade checkerboard teapot and cups" fetchpriority="high"><span class="corner-note">paint, sip, repeat</span></div></div></section>
<section class="section" id="menu-intro"><div class="container"><div class="menu-intro reveal"><div><span class="eyebrow">A little something for everyone</span><h2>What are you<br><span class="serif">in the mood for?</span></h2></div><p>From an all-day breakfast to grill favourites, pizza, coffee and something cold. Here’s a selection from the Casa Luano menu.</p></div><nav class="menu-jump" aria-label="Jump to menu section"><a href="#breakfast">Breakfast</a><a href="#small-plates">Small plates</a><a href="#grill">From the grill</a><a href="#pizza">Pizza & dessert</a><a href="#drinks">Drinks</a></nav></div></section>
{menu_group('breakfast', 'All-day<br><span class="serif">breakfast.</span>', 'For slow starts and late risers alike.', [
('Early Bee', 'Eggs, toast, charred tomato, mushrooms and bacon.', 'K170'),
('Fully Loaded', 'Eggs, toast, mushrooms, bacon, breakfast sausage and baked beans.', 'K200'),
('Breakfast Sandwich', 'Bacon, egg, sliced tomato and cheese in toasted bread.', 'K180'),
('Vegetable Omelette', 'Garden vegetables folded into a soft omelette.', 'K120')])}
{menu_group('small-plates', 'A little<br><span class="serif">something.</span>', 'For painting sessions, sharing and grazing around the table.', [
('Greek Style Salad', 'Fresh, crunchy salad with Luano honey-based dressing.', 'K70'),
('Casa Fusion Basket', 'A little bit of everything: croquettes, wings and crispy fries.', 'K180'),
('The Crunchy Basket', 'Chicken strips, croquettes and a portion of chips.', 'K230'),
('Bacon Loaded Fries', 'Fries smothered in molten cheese and crispy bacon.', 'K200')])}
{menu_group('grill', 'From the<br><span class="serif">fire.</span>', 'Clay, fire and Luano flavour.', [
('Casa Tandoori T-Bone', 'Flame-kissed steak in a signature tandoori seasoning.', 'K220'),
('Casa BBQ Pork Ribs', 'Juicy, charred ribs glazed in Luano BBQ sauce.', 'K250'),
('Luano Peri Peri Wings', 'Wings basted in house-made peri peri sauce.', 'K130'),
('Tandoori Chicken', 'Marinated chicken cooked in the Wildflower tandoor oven.', 'K130')])}
{menu_group('pizza', 'Share a slice.<br><span class="serif">Save dessert.</span>', 'The table has room for both.', [
('Classic Margherita Pizza', 'Tomato, mozzarella and basil.', 'K160'),
('Casa Meaty Pizza', 'Bacon, marinated chicken, spicy mince and mozzarella.', 'K250'),
('Chocolate Brownie', 'Fudgy chocolate brownie with vanilla honey ice cream.', 'K190'),
('Vanilla Luano Honey', 'Vanilla ice cream swirled with Luano honey.', 'K50')])}
{menu_group('drinks', 'Something<br><span class="serif">to sip.</span>', 'A cup in one hand, a paintbrush in the other.', [
('Cappuccino', 'A coffee classic for a slow afternoon.', 'K60'),
('Iced Latte', 'Vanilla, hazelnut or caramel.', 'K70'),
('Luano Ginger Honey Tea', 'Warming ginger and honey.', 'K70'),
('Homemade Lemonade', 'Bright and refreshing.', 'K60'),
('Classic Mojito', 'A fresh mocktail with citrus and mint.', 'K120'),
('Luano Zombie', 'A tropical house cocktail.', 'K180')])}
<section class="section" style="background:#efe9dc"><div class="container"><span class="eyebrow">A glimpse of the table</span><div class="menu-photo-strip"><figure><img src="assets/burger.jpg" alt="Burger photographed at Casa Luano" loading="lazy"><figcaption>For hearty appetites</figcaption></figure><figure><img src="assets/prawns.jpg" alt="Prawn plates photographed at Casa Luano" loading="lazy"><figcaption>For sharing</figcaption></figure><figure><img src="assets/wrap.jpg" alt="A wrap photographed at Casa Luano" loading="lazy"><figcaption>For one more bite</figcaption></figure></div><p class="price-note">Menu items and prices may change. Please check with Casa Luano.</p></div></section>
{info_band('Come hungry. Leave inspired.', 'Make a day of it: explore the clay experiences, then find your favourite spot at the café table.', 'Plan a visit', 'visit.html')}
'''


gather = f'''
<section class="page-hero gather-hero"><div class="container"><div class="reveal"><span class="eyebrow">For dates, friends and celebrations</span><h1>Get together.<br><span class="serif">Get creative.</span></h1><p>Some afternoons are better shared. Bring your favourite people for painting, making, food and all the conversations in between.</p>{button('Plan a gathering', '#gather-details', 'dark')}</div><div class="page-hero-photo reveal reveal-delay-1"><img src="assets/planters-collection.jpg" alt="Colourful handmade planters displayed on wooden stands" fetchpriority="high"><span class="corner-note">make it a day</span></div></div></section>
<section class="section gather-story"><div class="container gather-story-grid"><div class="reveal"><span class="eyebrow">Around the same table</span><h2>Come for the clay.<br><span class="serif">Stay for each other.</span></h2><p>Pottery painting is made for easy catch-ups, solo dates and soft afternoons with friends. Choose your pieces, spread out the paints and make room for snacks and drinks.</p><p>For special occasions, please enquire in advance so the team can help you plan your visit.</p>{button('See pottery painting', 'paint.html', 'outline')}</div><div class="gather-frame reveal reveal-delay-1"><img src="assets/painted-bowls.jpg" alt="A colourful set of handmade painted bowls" loading="lazy"><span class="hand">make memories, too</span></div></div></section>
<section class="section" id="gather-details"><div class="container"><div class="section-heading reveal"><div><span class="eyebrow">Make it your kind of day</span><h2>Good company.<br><span class="serif">Great stories.</span></h2></div><p>Choose the creative experience that fits your group, then add time around the café table.</p></div><div class="occasion-grid"><article class="occasion reveal"><span class="number">01</span><div><h3>Paint together</h3><p>Choose pieces from the Wildflower shelves and settle in with a palette.</p></div></article><article class="occasion reveal reveal-delay-1"><span class="number">02</span><div><h3>Try the wheel</h3><p>Book guided wheel throwing for a shared first spin.</p></div></article><article class="occasion reveal reveal-delay-2"><span class="number">03</span><div><h3>Stay for food</h3><p>Make time for a meal, a coffee or one more round.</p></div></article></div></div></section>
<section class="split-feature"><div class="feature-image"><img src="assets/frog-incense.jpg" alt="Whimsical frog incense holder in a painted scene" loading="lazy"></div><div class="feature-copy"><span class="eyebrow">A keepsake of the day</span><h2>Something to take<br>home together.</h2><p>The fun doesn't end when the brushes go down. Your painted pottery is glazed and fired, then ready to collect once the kiln has done its work.</p>{button('See how painting works', 'paint.html', 'light')}</div></section>
{info_band('Bring your people.', 'For groups and special occasions, contact Casa Luano in advance about the day you have in mind.', 'Find us on Instagram')}
'''


visit = f'''
<section class="page-hero visit-hero"><div class="container"><div class="reveal"><span class="eyebrow">Olympia · Lusaka</span><h1>There's a seat<br><span class="serif">for you here.</span></h1><p>Come for a coffee, stay for a brushstroke, and find out why a little time with clay can turn a whole day around.</p>{button('Get directions', 'https://www.google.com/maps/search/?api=1&query=Casa+Luano+Olympia+Lusaka', 'dark', True)}</div><div class="page-hero-photo reveal reveal-delay-1"><img src="assets/buddha-planter.jpg" alt="Handmade ceramic planter and sculptural figure with succulents" fetchpriority="high"><span class="corner-note">find your way in</span></div></div></section>
<section class="section"><div class="container visit-story"><div class="reveal"><span class="eyebrow">Our little corner of Lusaka</span><h2>A space to<br><span class="serif">unwind and make.</span></h2><p>Casa Luano began with a vision for a space where community could come together to be creative, unwind and enjoy a memorable experience. Art, nature, good company and good food all belong at the same table.</p><p>Wildflower Ceramics brings the clay: handmade pottery to paint and guided time on the wheel. Casa Luano brings the room to relax and make a day of it.</p>{button('Choose an experience', 'index.html#experiences', 'outline')}</div><img class="reveal reveal-delay-1" src="assets/checker-tea-set.jpg" alt="A playful handmade tea set from Wildflower Ceramics" loading="lazy"></div></section>
<section class="section maker-film-section"><div class="container maker-film-grid"><div class="reveal"><span class="eyebrow">A maker's eye</span><h2>Every piece begins<br><span class="serif">with a pair of hands.</span></h2><p>Behind the painted shelves are makers with a love of shaping, glazing and giving clay its own character. Take a glimpse into the process.</p><p>Press play to watch a short Wildflower Ceramics film.</p></div><figure class="maker-film reveal reveal-delay-1"><video controls playsinline preload="none" poster="assets/buddha-planter.jpg" aria-label="Short film showing a Wildflower Ceramics piece"><source src="assets/maker-story.mp4" type="video/mp4"></video><figcaption>A little story from the studio</figcaption></figure></div></section>
<section class="section" style="background:#eee9dd"><div class="container"><div class="section-heading reveal"><div><span class="eyebrow">The useful bits</span><h2>Before you<br><span class="serif">come over.</span></h2></div></div><div class="visit-info"><article><h3>Where</h3><p>Njoka Road, Olympia<br>Lusaka, Zambia</p></article><article><h3>When</h3><p>Tuesday–Sunday<br>7am–9pm</p></article><article><h3>Plan ahead</h3><p>Pottery painting walk-ins welcome.<br>Enquire in advance for wheel sessions and special occasions.</p></article></div><p class="price-note">Opening hours may change; check Casa Luano’s Instagram before visiting.</p></div></section>
<section class="map-panel" aria-label="Find Casa Luano in Olympia, Lusaka"><div class="map-card"><span class="map-pin" aria-hidden="true">⌖</span><span class="eyebrow">Olympia, Lusaka</span><h2>Find Casa Luano</h2><p>Njoka Road, Olympia, Lusaka</p>{button('Open directions', 'https://www.google.com/maps/search/?api=1&query=Casa+Luano+Olympia+Lusaka', 'dark', True)}</div></section>
{info_band('Come clay with us.', 'Follow the café for the latest sessions, menu updates and opening details.', 'Visit Instagram')}
'''


PAGES = {
    "index.html": ("A little clay, a lot of joy", "Paint pottery, try the wheel and enjoy food and drinks at Casa Luano by Wildflower in Lusaka.", home, "home"),
    "paint.html": ("Pottery painting", "Choose a handmade piece and paint it at Casa Luano by Wildflower in Lusaka.", paint, "paint"),
    "wheel.html": ("Wheel throwing workshops", "Try a guided wheel throwing workshop with Wildflower Ceramics at Casa Luano in Lusaka.", wheel, "wheel"),
    "menu.html": ("Food and drink", "Browse a selection of food and drinks from the Casa Luano café menu.", menu, "menu"),
    "gather.html": ("Gather at Casa Luano", "Plan a creative day with friends, dates or a group at Casa Luano in Lusaka.", gather, "gather"),
    "visit.html": ("Visit Casa Luano", "Find Casa Luano by Wildflower in Olympia, Lusaka and explore its clay café experiences.", visit, "visit"),
}

for filename, (title, description, content, page) in PAGES.items():
    (ROOT / filename).write_text(base(page, title, description, content), encoding="utf-8")

(ROOT / "favicon.svg").write_text('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="15" fill="#26231e"/><g fill="#efbd25">''' + ''.join(f'<ellipse cx="32" cy="18" rx="4" ry="11" transform="rotate({i*30} 32 32)"/>' for i in range(12)) + '''<circle cx="32" cy="32" r="9"/></g></svg>''', encoding="utf-8")

print(f"Built {len(PAGES)} pages in {ROOT}")
