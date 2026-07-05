# Chapter 2. A Short History of Artificial Intelligence

## The Amnesia Problem

The technology industry has a peculiar relationship with its own past: it forgets it. Every few years, a new generation of founders, investors, and pundits emerges convinced that they are living through a uniquely transformative moment — one that has no precedent, obeys no historical pattern, and will unfold faster and more completely than anything that came before.

They are always wrong. And they are always half-right.

The half-right part is that something genuinely new is happening. The wrong part is the belief that this time is different in kind, not merely in degree. If you want to understand where AI is going, you need to understand where it has been. Not because history repeats exactly — it does not — but because history rhymes. The forces that drove previous waves of AI enthusiasm and disappointment are the same forces operating today. The investors who poured money into expert systems in the 1980s were animated by the same mix of genuine technological progress and wild overpromising that animates the venture capitalists writing billion-dollar checks to AI labs in 2026. The researchers who warned in 1973 that AI was hitting fundamental limits were making the same category of error as the researchers today who claim we are on the verge of artificial general intelligence: they were extrapolating from the present into a future they could not see.

This chapter is a short history. It is not comprehensive — whole books have been written about individual years in AI research — but it covers what you need to know to avoid the amnesia trap. The three waves of AI development. The two winters that nearly killed the field. And the uncomfortable truth that the current wave, for all its genuine novelty, is following a script written decades ago.

---

## Wave One: Symbolic AI (1950s–1980s)

### The Founding Fathers

The story begins, as these stories often do, with a meeting. In the summer of 1956, a young mathematician named John McCarthy gathered ten researchers at Dartmouth College for a two-month workshop. The proposal was audacious: they would study "the conjecture that every aspect of learning or any other feature of intelligence can in principle be so precisely described that a machine can be made to simulate it." McCarthy needed a name for this field, and he chose one that would shape public imagination for the next seventy years: artificial intelligence.

The name was a triumph of marketing and a curse of expectation. "Intelligence" is a word we use for minds — for beings that think, understand, and want. By calling their field artificial intelligence, the founding researchers invited the public to treat their machines as minds. The machines were not. They were logic engines, and the gap between logic and intelligence would define the first wave.

The early work was genuinely impressive. In 1957, Herbert Simon and Allen Newell created the Logic Theorist, a program that proved mathematical theorems from Principia Mathematica. It was, in Simon's words, "the first machine to think." It was not thinking, of course — it was searching through logical rules to find derivations — but the output looked like thinking, and that was enough to capture imaginations.

The dominant approach of this era was symbolic AI: the belief that intelligence could be encoded as rules, symbols, and logical relationships. If you could write down all the rules that govern a domain — medicine, chess, language — you could build a machine that performed as well as an expert. This was the expert systems approach, and for a brief period in the 1970s and 1980s, it attracted enormous investment.

### Expert Systems: The Promise and the Brittle Reality

The most famous expert system was MYCIN, developed at Stanford in the 1970s. MYCIN diagnosed bacterial infections and recommended antibiotics. It worked by asking a doctor a series of questions — patient symptoms, lab results, risk factors — and then consulting a knowledge base of roughly 600 if-then rules to arrive at a diagnosis. When tested, MYCIN performed as well as infectious disease specialists in its narrow domain.

This was genuinely useful. But it was also fundamentally limited. MYCIN knew nothing about medicine outside bacterial infections. It could not learn from new cases. It could not handle exceptions that its programmers had not anticipated. And the effort required to encode expertise as rules was staggering: researchers estimated that it took a "knowledge engineer" roughly a year to encode the expertise of a single domain expert into a usable rule set.

The problem was what philosophers call the "frame problem" and what engineers call "common sense." A human doctor knows, without being told, that a patient cannot be in two places at once, that drugs have side effects, that patients sometimes lie about their symptoms, and that medical knowledge evolves. MYCIN knew none of this. It knew only the 600 rules it had been given, and it applied them with mechanical precision regardless of context.

Other expert systems followed the same pattern. DENDRAL analyzed chemical compounds. PROSPECTOR predicted mineral deposits. XCON configured computer systems for Digital Equipment Corporation, reportedly saving the company $40 million annually. Each was impressive in its domain. Each was helpless outside it. And each required enormous human effort to build and maintain.

### ELIZA: The First Chatbot and the First Illusion

In 1966, a decade before MYCIN, MIT researcher Joseph Weizenbaum created ELIZA — a program that simulated a Rogerian psychotherapist. ELIZA worked by pattern matching: it scanned the user's input for keywords and responded with pre-written phrases or reflected the user's statements back as questions. If you typed "I am sad," ELIZA might reply, "How long have you been sad?" If you typed "My mother hates me," it might reply, "Tell me more about your mother."

Weizenbaum created ELIZA as a demonstration of how superficial human-computer interaction could be. He was horrified when people began treating it as a genuine therapeutic tool. His own secretary reportedly asked him to leave the room so she could have a private conversation with the program. The phenomenon Weizenbaum observed — humans attributing understanding and empathy to a pattern-matching machine — would repeat with ChatGPT sixty years later. The technology changed dramatically. The human tendency to see minds in machines did not.

### The Hype

If you want to understand the first AI bubble, consider a prediction made by Herbert Simon in 1965: "Machines will be capable, within twenty years, of doing any work a man can do." Marvin Minsky, another founding figure, predicted in 1970 that "in from three to eight years we will have a machine with the general intelligence of an average human being." These were not fringe figures. Simon won the Nobel Prize in Economics. Minsky co-founded MIT's AI laboratory. They were the smartest people in the room, and they were wrong by decades.

The overpromising was not cynical. It was sincere. The researchers genuinely believed that the progress they had seen in narrow domains — theorem proving, game playing, pattern recognition — would generalize to full human intelligence. They underestimated the complexity of common sense, the importance of embodied experience, and the sheer scale of computation that would eventually be required. Their error was not dishonesty. It was extrapolation.

---

## The First AI Winter (1970s)

By the early 1970s, the gap between promise and reality had become impossible to ignore. The Lighthill Report, commissioned by the British government in 1973, delivered a devastating assessment: AI research had failed to deliver on its core objectives, and the combinatorial explosion of possibilities in real-world problems made the symbolic approach intractable. Funding dried up. Research programs were cancelled. Graduate students stopped applying to AI labs. The field entered what researchers grimly called an "AI winter."

The winter was not total. Work continued in isolated pockets. But the public narrative shifted from "AI will transform everything" to "AI was oversold." The shift was not entirely fair — real progress had been made — but it was understandable. When you promise thinking machines and deliver rule-based diagnostic systems that require a year of manual coding per domain, the disappointment is proportionate to the hype.

The first winter teaches a lesson that remains relevant: **AI winters do not kill good technology. They kill overpromised timelines.** The ideas developed in the 1960s and 1970s — knowledge representation, search algorithms, logical inference — would resurface in later decades, often in forms the original researchers could not have imagined. What died in the first winter was not the research but the expectation that human-level intelligence was a few years away.

---

## Wave Two: Machine Learning (1990s–2010s)

### The Paradigm Shift

The second wave of AI was defined by a simple but profound shift in approach. Instead of programming machines with explicit rules, researchers began building machines that learned patterns from data.

The shift was partly philosophical and partly pragmatic. Philosophically, researchers realized that encoding common sense as rules was a dead end — there were too many rules, too many exceptions, too much tacit knowledge that humans possessed but could not articulate. Pragmatically, the internet was creating datasets of a scale that had never existed before, and statistical methods were proving surprisingly effective at finding useful patterns in those datasets.

The tools of this era were statistical and probabilistic: neural networks, support vector machines, random forests, Bayesian networks. These were not new ideas — neural networks dated back to the 1940s — but they had been limited by computational constraints. By the 1990s, computers were fast enough to make them practical for real problems.

### What Actually Worked

The machine learning era produced technologies that are now so embedded in daily life that we barely notice them. Spam filters that learn to recognize junk mail from examples rather than from programmed rules. Recommendation systems that predict what you will buy based on what people like you have bought. Credit card fraud detection that flags unusual transactions by learning patterns of legitimate use. Search engines that rank web pages by learning which results users actually click.

These systems were narrow, specialized, and limited. A spam filter could not write poetry. A recommendation engine could not drive a car. But they worked, reliably and at scale, in ways that expert systems never had. They did not require teams of knowledge engineers to encode rules. They required data, and the internet was producing data in unprecedented volumes.

The key insight of this era was that **intelligence could emerge from statistics rather than from logic.** You did not need to teach a machine the rules of grammar to build a decent speech recognizer. You could feed it thousands of hours of audio and let it learn the statistical relationships between sounds and words. The results were messy, probabilistic, and occasionally wrong — but they were good enough to be useful, and they improved as more data became available.

### The Neural Network Revival

Neural networks — computational models loosely inspired by the structure of biological brains — had been a fringe approach for decades. They fell out of favor after Marvin Minsky and Seymour Papert's 1969 book *Perceptrons* demonstrated serious theoretical limitations of the simplest network architectures. But by the 1990s, researchers had developed more sophisticated architectures — multi-layer networks, backpropagation training, convolutional layers — that overcame many of those limitations.

The results were impressive but narrow. In 1997, IBM's Deep Blue defeated chess champion Garry Kasparov in a highly publicized match. The victory was symbolic — a machine had beaten the best human at a game long considered a benchmark of intelligence — but the method was brute force. Deep Blue evaluated 200 million positions per second using specialized hardware and handcrafted evaluation functions. It was not learning. It was calculating. And it could do nothing else.

The second wave was characterized by this tension: genuine progress in narrow domains, coupled with continued failure to generalize. Machine learning worked for spam filters and recommendation engines. It did not work for open-ended conversation, common-sense reasoning, or general problem-solving. The field made money and produced useful tools, but it did not produce intelligence.

---

## The Second AI Winter (Late 1980s–Early 1990s)

The second winter was less dramatic than the first but more commercially significant. Expert systems — the great commercial hope of the 1980s — were failing to deliver on their economic promises. The cost of developing and maintaining rule-based systems was higher than anticipated. The systems were brittle, unable to handle situations their programmers had not foreseen. And the knowledge acquisition bottleneck — the need to manually encode expert knowledge — proved intractable for many domains.

Companies that had invested heavily in expert systems technology quietly abandoned their projects. The term "AI" became toxic in business contexts; researchers began using euphemisms like "intelligent systems" or "knowledge-based systems" to avoid association with the hype. Venture funding collapsed. AI startups disappeared.

The second winter, like the first, did not kill the underlying technology. The statistical methods developed in the 1990s would form the foundation for everything that followed. What died was the business model of selling "expertise in a box" and the belief that rule-based systems could scale to real-world complexity.

---

## Wave Three: Deep Learning and Transformers (2010s–Present)

### The ImageNet Moment

The third wave began with a competition and a GPU.

In 2012, a team from the University of Toronto led by Geoffrey Hinton entered the ImageNet Large Scale Visual Recognition Challenge — an annual competition to classify images into thousands of categories. Their entry, a deep neural network called AlexNet, achieved an error rate of 15.3%. The second-best entry achieved 26.2%. The gap was unprecedented.¹

AlexNet's success was not due to a new algorithmic breakthrough. Deep neural networks had existed for decades. What changed was the hardware: Hinton's team trained AlexNet on two NVIDIA GPUs, exploiting their parallel processing power to train a network with 60 million parameters — far larger than anything previously attempted. The GPUs made the computation feasible. The massive dataset made the network generalize. And the depth of the network — eight layers, compared to two or three in earlier approaches — allowed it to learn hierarchical features: edges in early layers, textures in middle layers, object parts in deeper layers.

The ImageNet result sent shockwaves through computer science. Within three years, every entry in the competition was using deep learning. Within five years, deep learning had conquered speech recognition, machine translation, and game playing. Within ten years, it had produced the large language models that dominate public discourse today.

### The Transformer Revolution

The second pivotal moment came in 2017. A team at Google Brain published a paper with the deceptively modest title "Attention Is All You Need." The paper introduced a new neural network architecture called the transformer, which replaced the sequential processing of earlier language models with a mechanism called self-attention.

The details of how transformers work belong in Chapter 3. What matters for this history is the consequence: transformers made it possible to train language models at a scale that had previously been impossible. Earlier approaches processed text one word at a time, like a person reading a sentence from left to right. Self-attention allowed models to look at every word in a sentence simultaneously, understanding context and relationships in ways that sequential models could not match.

The result was an explosion in model size and capability. GPT-2 (2019) had 1.5 billion parameters. GPT-3 (2020) had 175 billion. GPT-4 (2023) reportedly had over a trillion, deployed across a mixture of expert models. GPT-5 arrived in August 2025, and by 2026 the frontier had shifted again with Claude 4, Gemini 3, and Llama 4. Each increase in scale produced emergent capabilities — abilities that were not explicitly programmed but arose from the statistical relationships learned at massive scale.

### ChatGPT and the Mainstreaming of AI

On November 30, 2022, OpenAI released ChatGPT — a conversational interface built on top of GPT-3.5. The release was almost accidental; it was described internally as a "research preview." Within five days, it had one million users. Within two months, it had 100 million.²

The significance of ChatGPT was not technical but experiential. AI had been powering search engines, recommendation systems, and spam filters for years, but it had been invisible to most users. ChatGPT made AI tangible. You could type a question and get a human-sounding answer. You could ask it to write a poem, debug code, summarize a document, or plan a vacation. The quality was uneven — it confidently generated falsehoods, misunderstood context, and produced generic prose — but the experience was mesmerizing in a way that no previous AI system had been.

ChatGPT accomplished what ELIZA had demonstrated sixty years earlier: humans are predisposed to see intelligence in fluent language. The difference was that ELIZA's responses were obviously mechanical to anyone who interacted with it for more than a few minutes. ChatGPT's responses could fool experts. The illusion was vastly more compelling — and vastly more dangerous.

### The Agentic Turn (2025–2026)

By 2025, the conversation had shifted from chatbots to agents. Researchers and companies began building systems that could not just generate text but take action: search the web, execute code, book appointments, and coordinate multi-step workflows. Multi-agent systems — networks of specialized AI agents that collaborated on complex tasks — moved from research papers to product roadmaps.

This is where we are now. The third wave is still cresting. Whether it crashes — whether we face a third AI winter — depends on whether the current capabilities can be translated into reliable, economically viable systems, or whether the gap between demo and deployment proves as intractable as it did for expert systems forty years ago.

---

## What the Winters Teach Us

### Hype Is a Constant; Progress Is a Trend

If you graph AI capability over time, you get a jagged line: long plateaus punctuated by sudden jumps, followed by periods of inflated expectation, followed by disappointment, followed by renewed progress. The long-term trend is unmistakably upward. The short-term cycles are brutal.

The first winter killed the belief that logic engines would soon think like humans. The second winter killed the belief that expert systems would capture human expertise in rule-based form. Neither killed the research programs that eventually produced the technologies we use today. Search algorithms from the 1970s evolved into Google. Statistical methods from the 1990s evolved into modern recommendation systems. Neural network research from the 1980s — conducted in obscurity during the second winter — evolved into deep learning.

The pattern is this: **hype is a constant, but progress is a trend.** The people who survive the winters are not the ones who bet everything on the peak of the hype cycle. They are the ones who understand that real capability accumulates slowly, that demonstrations are not products, and that the boring work of engineering matters more than the exciting work of speculation.

### The Implementation Gap

One pattern repeats across all three waves: the gap between what AI can demonstrate in a controlled setting and what it can deploy reliably in the real world is always larger than enthusiasts predict.

Expert systems could diagnose bacterial infections in a laboratory setting but failed in messy clinical environments. Machine learning could classify images accurately in competitions but struggled with lighting variations, occlusions, and edge cases in production. Large language models can write fluent essays in a chat interface but produce unreliable output when integrated into business workflows.

A 2026 study by the HR technology company Gloat found that 95% of AI pilot projects in enterprises failed to move to production.³ This is not a new problem. It is the same implementation gap that plagued expert systems in the 1980s, dressed in new clothing.

### Capital Follows Hype; Capability Follows Time

The most dangerous moment in any technology cycle is when capital arrives before capability. In the first wave, government funding poured into AI labs based on Simon's and Minsky's predictions. In the second wave, venture capital funded expert system companies that could not scale. In the third wave, billions of dollars have flowed into AI startups and foundation model companies, many of which have no defensible technology and no viable business model.

Capital accelerates development, but it also accelerates hype. When investors expect returns on compressed timelines, companies have incentives to overpromise. When overpromising meets the implementation gap, disappointment follows. And disappointment, when it is large enough, produces winter.

---

## Why This Wave Is Different (And Why It Is Also the Same)

### What Is Different

The current wave differs from its predecessors in four important ways.

**Scale of computation.** The amount of compute used to train modern AI models is staggering. GPT-4 reportedly required computational resources that would have been unimaginable a decade ago, costing tens of millions of dollars in electricity and hardware alone. This scale produces capabilities — emergent reasoning, few-shot learning, code generation — that smaller models cannot replicate.

**Scale of data.** The internet has produced a corpus of human-generated text, images, and video that dwarfs anything available to previous generations of researchers. Large language models train on trillions of words — a significant fraction of all text ever digitized. This data abundance is unprecedented and, for now, irreproducible.

**Scale of capital.** AI investment in 2025 and 2026 exceeds the total investment in all previous AI waves combined. The largest AI labs have raised billions of dollars. Governments have declared AI a strategic priority. The economic stakes are incomparably higher than they were in the 1970s or 1990s.

**Consumer accessibility.** Previous AI technologies were invisible to ordinary users. Machine learning powered your spam filter and your search results, but you did not interact with it directly. Large language models are different. Hundreds of millions of people use them daily. The democratization of access means that AI hype and AI reality are now experienced by the general public, not just by researchers and investors.

### What Is the Same

For all these differences, the current wave repeats patterns that should be familiar by now.

**Hype exceeds reality.** Claims about imminent AGI, AI consciousness, and the obsolescence of human labor are as overblown as Simon's prediction that machines would do "any work a man can do" by 1985. The technology is genuinely impressive. The claims made about it are often absurd.

**Underestimated implementation challenges.** The 95% pilot failure rate suggests that moving from demonstration to deployment remains as difficult as it was for expert systems. The challenges have changed — bias, hallucination, security, cost — but the fundamental gap between "works in a demo" and "works in production" persists.

**Overconfidence in near-term capabilities.** Every wave has produced researchers and investors who believe that the current approach, scaled sufficiently, will produce general intelligence. In the 1960s, it was symbolic logic. In the 1990s, it was neural networks with a few thousand neurons. Today, it is transformers with trillions of parameters. The scaling hypothesis — that bigger models will simply keep getting smarter — may be correct. History suggests caution.

---

## The Long View

If you take a sufficiently long perspective — decades rather than years — the story of AI is one of relentless, uneven progress. The field has gone through two winters and may yet face a third. But each winter has been followed by a spring that exceeded the previous summer. The algorithms developed in obscurity during the 1980s neural network winter became the foundation for deep learning. The statistical methods developed during the 1990s became the foundation for modern machine learning infrastructure.

The question is not whether AI will keep advancing. It will. The question is whether the current pace of advance is sustainable, whether the economics of massive models will prove viable, and whether the public and private investments being made today will produce returns proportionate to their scale. On these questions, history is less encouraging. The history of technology is littered with periods when genuine progress was derailed by hype, misallocated capital, and unrealistic expectations.

The antidote to hype is not cynicism. Cynicism is just hype in reverse — the belief that nothing will work because something did not work before. The antidote is historical perspective: the recognition that progress is real, that cycles are inevitable, and that the people who navigate both the peaks and the valleys with clear eyes are the ones who thrive.

---

## Endnotes

¹ A. Krizhevsky, I. Sutskever, and G. E. Hinton, "ImageNet Classification with Deep Convolutional Neural Networks," *Advances in Neural Information Processing Systems* 25 (NIPS 2012). AlexNet's top-5 e...

² OpenAI internal data, reported in multiple sources. ChatGPT reached 1 million users in five days after its November 30, 2022 launch, and 100 million monthly active users by January 2023, making it th...

³ Gloat, "The State of AI in the Enterprise 2026," HR technology industry report. The 95% pilot-to-production failure rate reflects technical, organisational, and cultural barriers rather than...

---

## Key Takeaway

AI history is a cycle of hype, disappointment, and permanent advance. The winters do not kill good ideas; they kill overpromised timelines. The current wave is different in scale — of computation, data, capital, and public access — but it is following a script written decades ago. The organizations and individuals who survive will not be the ones who bet everything on the peak of the hype cycle. They will be the ones who understand that capability accumulates slowly, that demonstrations are not products, and that the boring work of engineering matters more than the exciting work of speculation.


---

