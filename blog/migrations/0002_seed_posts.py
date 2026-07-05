from django.db import migrations
from django.utils import timezone


def seed_posts(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')

    posts = [
        {
            'title': 'What Is AI Actually? A Skeptic\'s Guide for Business Owners',
            'slug': 'what-is-ai-actually',
            'category': 'ai-explained',
            'excerpt': 'Stop confusing "AI" with "magic." Here\'s what large language models, neural networks, and machine learning actually do\u2014and what they absolutely cannot do.',
            'body': """If you've made it past 2023 without someone trying to sell you an "AI-powered" solution, you're either extraordinarily lucky or you don't have an email address.

Every vendor pitch now leads with "AI." Every startup claims to be "AI-native." Every consultant wants to sell you an "AI transformation."

Here's the uncomfortable truth: most of them are lying to you. Not deliberately, necessarily. But they're using the term "AI" the way a magician uses smoke \u2014 to obscure what's actually happening behind the curtain.

So let's cut through it. What is AI, actually? And more importantly, what isn't it?

## The Three Things "AI" Actually Means

When someone says "AI" in a business context, they usually mean one of three things:

**1. Large Language Models (LLMs)** like GPT-4, Claude, and Gemini. These are pattern-matching engines trained on enormous amounts of text. They don't "understand" anything. They predict what words should come next, based on statistical patterns in their training data. They're incredibly good at generating plausible-sounding text. They're also incredibly good at generating plausible-sounding nonsense.

**2. Machine Learning (ML)** systems that learn from data to make predictions. Think recommendation engines, fraud detection, demand forecasting. These work by finding statistical patterns in historical data and extrapolating. They're powerful when the future looks like the past. They're dangerous when it doesn't.

**3. Traditional Software with a Marketing Budget.** This is the most common category. A company takes a basic automation tool, adds a sprinkle of ML (or just claims to), and calls it "AI-powered." Most "AI" in business falls into this bucket.

## What AI Cannot Do (No Matter What the Vendor Says)

**Reason from first principles.** An LLM can tell you what other people have said about a problem. It cannot think through a novel problem step-by-step in a way that guarantees correctness.

**Access real-time information** unless explicitly connected to live data sources. GPT-4's training data has a cutoff. It doesn't know what happened yesterday unless you feed it that information.

**Guarantee accuracy.** LLMs hallucinate. They make things up. They cite sources that don't exist. They confidently assert falsehoods. This isn't a bug you can patch out \u2014 it's fundamental to how they work.

**Replace judgment.** AI can give you options. It can summarize data. It cannot decide what matters to your business, what your customers actually want, or what risks are worth taking.

## The Framework That Actually Helps

Stop asking "Should we use AI?" Start asking: "What specific task are we trying to accomplish, and is an AI system the most reliable, cost-effective way to accomplish it?"

Here's the decision tree I use with clients:

1. **Is the task well-defined with clear success criteria?** If no, AI probably won't help.
2. **Do we have good historical data?** If no, ML won't work.
3. **Is the cost of being wrong low?** If no, don't use an LLM for it.
4. **Can a human verify the output quickly?** If no, don't automate it yet.
5. **Is the current manual process actually a bottleneck?** If no, don't fix what isn't broken.

## The Real Opportunity

The businesses winning with AI right now aren't the ones with the fanciest models. They're the ones that understand AI's limitations and design around them.

They use LLMs for first drafts, not final products. They use ML for recommendations, not decisions. They keep humans in the loop for anything that matters.

That's the partnership model. And it's the only model that works.

---

*Want the full framework? [Pre-order the book](/book/) for the complete implementation guide.*""",
            'reading_time_minutes': 6,
            'published': True,
            'published_at': timezone.now(),
            'meta_title': 'What Is AI Actually? A Skeptic\'s Guide',
            'meta_description': 'Stop confusing AI with magic. Here\'s what large language models and machine learning actually do\u2014and what they absolutely cannot do.',
        },
        {
            'title': 'Will AI Take My Job? An Honest Answer (With Numbers)',
            'slug': 'will-ai-take-my-job',
            'category': 'future-of-work',
            'excerpt': 'Everyone\'s asking. No one\'s answering honestly. Here\'s what the data actually says about AI, automation, and your career\u2014without the panic or the propaganda.',
            'body': """"Will AI take my job?"

I've been asked this question at least a hundred times since ChatGPT launched. By friends, by clients, by nervous executives, by confident twenty-somethings. Everyone wants a straight answer.

Here's the most honest one I can give you: **it depends on what you mean by "your job."**

## The Question Everyone's Really Asking

When people ask if AI will take their job, they're usually picturing a binary outcome: either they keep working exactly as they do now, or a robot replaces them and they're unemployed.

That's not how this works. That's never how technology works.

What actually happens is messier, more gradual, and more specific to your role than any headline can capture.

## What the Data Actually Says

Let's look at what we actually know, not what feels true.

**Historical precedent:** Automation has consistently eliminated specific *tasks*, not entire *jobs*. ATMs didn't eliminate bank tellers \u2014 they changed what tellers do. Excel didn't eliminate accountants \u2014 it changed what accountants do. The spreadsheet actually *increased* demand for people who could analyze numbers, because analysis became cheaper and more accessible.

**Current research on LLMs:** Studies from OpenAI, Goldman Sachs, and academic researchers estimate that 25-50% of current work tasks *could* be exposed to AI automation. But "exposed to automation" is not the same as "will be automated." And "automated" doesn't mean "eliminated."

**The actual impact so far:** Despite all the hype, unemployment rates in knowledge-work economies remain near historic lows. Companies are hiring people who can work *with* AI, not replacing people *with* AI.

## The Roles Most at Risk (And Why)

Let's be specific. Here are the roles where I see genuine displacement risk in the next 3-5 years:

**1. Pure content mills.** If your job is to produce generic, formulaic content at high volume with minimal quality standards, AI can already do 80% of what you do. This includes some SEO content writing, basic translation, and template-based copywriting.

**2. Entry-level data processing.** Roles that involve moving data between formats, basic cleaning, and simple categorization are being rapidly automated.

**3. Routine customer service.** First-line support for simple, repetitive queries is increasingly handled by AI systems.

**4. Basic graphic design for templated materials.** Logo generators, social media template tools, and automated design systems are eating the bottom of this market.

Notice what these have in common: they're roles where the work is *already* somewhat mechanical. AI accelerates a trend that was already happening.

## The Roles That Are Expanding

**AI implementation specialists.** Companies desperately need people who understand both the business problem and the AI tool well enough to connect them. This is the fastest-growing category I've seen.

**AI-savvy generalists.** The lawyer who can use AI to draft contracts faster. The marketer who can use AI to generate variations and test them. The analyst who can use AI to explore data they couldn't previously access. These people are becoming dramatically more productive \u2014 and valuable.

**Human judgment roles.** Strategy, ethics, creative direction, relationship management, negotiation, leadership. These don't just survive AI \u2014 they become more important as AI handles the routine work.

**AI quality assurance.** Someone has to check the AI's work. Someone has to train it. Someone has to decide when it's wrong. These are growing fields.

## What You Should Actually Do

Here's my practical advice, based on 12+ years of watching technology reshape industries:

**1. Learn to use AI for your specific role.** Not "learn about AI." Learn to *use* it. Spend 30 minutes a day for two weeks experimenting with tools relevant to your work. That's enough to get past the novelty phase and into genuine productivity gains.

**2. Develop the skills AI can't replicate.** Critical thinking, creative problem-solving, emotional intelligence, ethical judgment, relationship building. These aren't soft skills \u2014 they're the core competitive advantage of humans in an AI world.

**3. Specialize.** General knowledge work is increasingly commoditized by AI. Deep expertise in a specific domain, combined with AI fluency, is incredibly valuable.

**4. Build a portfolio of proof.** Document what you've accomplished with AI. Case studies, metrics, before/after comparisons. This is what gets you hired or promoted.

## The Honest Bottom Line

AI won't eliminate your job. But it will change what your job entails. The people who thrive are the ones who adapt faster than their competitors \u2014 not the ones who wait to see what happens.

The question isn't "Will AI take my job?" The question is "Will I be one of the people who knows how to use AI better than the person who replaces me?"

That part is entirely up to you.

---

*Want the full career framework? [Take the AI Readiness Scorecard](/readiness-scorecard/) to see exactly where you stand.*""",
            'reading_time_minutes': 8,
            'published': True,
            'published_at': timezone.now(),
            'meta_title': 'Will AI Take My Job? An Honest Answer With Data',
            'meta_description': 'What the data actually says about AI, automation, and your career\u2014without the panic or the propaganda.',
        },
    ]

    for p in posts:
        Post.objects.create(**p)


def reverse_seed(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    Post.objects.filter(slug__in=['what-is-ai-actually', 'will-ai-take-my-job']).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_posts, reverse_seed),
    ]
