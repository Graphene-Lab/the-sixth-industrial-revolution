
# Appendix B --- The Projects Behind the Vision, and Further Reading

## The Lab

The technologies described throughout this book are not hypothetical. They are being built, published, and refined by a small research lab, **AI Technology Graphene-Lab**, that prefers to let the machines speak for themselves. Its work is published openly on GitHub, under permissive licenses, precisely so that readers of this book can look, test, and --- if they choose --- adopt. This appendix points the reader to the real repositories that ground the chapters above, and then to a few books and writings for those who want to go further, whether in the direction of the machine, the cloud, or the agent.

The whole lab's projects are gathered at: **https://github.com/orgs/Graphene-Lab/repositories**. Below are the specific ones that appear in this book.

## The Projects in This Book

### AgentBridge --- the agentic assistant that knows your business

**Repository:** https://github.com/Graphene-Lab/AgentBridge

AgentBridge is a self-hosted AI personal assistant that automates office work without sacrificing privacy. It runs its own agents behind two interfaces in one process --- a full-screen chat terminal, and an HTTP API that speaks the standard OpenAI protocol, so any OpenAI-compatible client can drive the same agents. Its defining idea is that an agent's abilities are compiled assemblies loaded as plugins, so the agent calls software directly rather than over a protocol. It carries a proprietary deterministic memory (it never forgets the facts, people, and documents it has handled), runs inside a native sandbox so its actions are bounded and reversible, and can be supplied with the private cloud so the knowledge it reads never leaves the company. The lab describes it as the tool behind this book --- the one that makes the "office at midnight" real.

### CloudServer --- the private, trustless, zero-knowledge cloud

**Repository:** https://github.com/Graphene-Lab/CloudServer

CloudServer is the private cloud kept inside the company. Where the public cloud centralizes data in giant data centers that can be read --- or compelled to read --- a private, zero-knowledge cloud like CloudServer keeps the data under the company's own control, so that the telemetry flowing from the machines never leaves the company's authority and is never readable by a third party. This is the answer, for the factory, to the privacy failures exposed by the great data scandal of the early 2010s.

### UISupportBlazor --- deterministic AI for automatic front-ends and APIs

**Repository:** https://github.com/Graphene-Lab/UISupportBlazor

UISupportBlazor is a pioneering agentic-AI-for-coding project, but its deeper significance is conceptual: it demonstrates that a compiled assembly --- the exact, complete specification of a backend --- can be used as the ultimate deterministic prompt, from which user interfaces and API layers are derived with mathematical certainty rather than guessed from a natural-language prompt. It is the flagship example of the "two kinds of mind" argument (Chapter 13) and the "assembly as the last truth" argument (Chapter 14): the deterministic mind, where certainty is required.

### The deterministic-AI support libraries

Beyond these headline projects, the lab publishes the support libraries that make the whole stack coherent --- for example the assembly-analysis tooling (UISupportGeneric, GiraffeAI) that lets a machine read a compiled assembly and derive from it the interface or tool it needs. Together, these form an ecosystem rather than a set of isolated tools, and that ecosystem is what the book is ultimately describing.

## The Telegram Door

The work is shown, not merely described, on the lab's Telegram channel. The QR code in [A Note About the Book](preface.md) --- and again in the [Epilogue](epilogue-the-factory-that-dreamed.md) --- leads there. If you want to see the machine that thinks, the cloud that keeps its secret, the agent that knows your business, and the humanoid that walks onto the floor as they are, in real time, that is the door.

## Further Reading

For those who wish to widen the horizon beyond this book, a few directions offer particularly rich ground. These are suggestions, not a required reading list; pick the path that matches where you stand.

**On the history of revolutions and intelligence.** The reader who wants to place the sixth revolution in the long arc will find much worth reading in the histories of the earlier waves --- the steam engine, the assembly line, the computer --- and in the longer history of AI itself, with its winters and its springs. The pattern those histories reveal is the same decision-tool this book offers: know the pattern, and you are harder to fool.

**On the two kinds of mind.** The distinction between the probabilistic mind and the deterministic mind is the deepest idea in this book, and it is worth reading about in its original contexts: the theory of computation and the deterministic nature of compilation, on one side; and machine learning, on the other. The lab's own writings on deterministic AI (see UISupportBlazor above) push this idea further than this book can, and are the natural next step for the reader who finds the two-minds argument compelling.

**On privacy and the cloud.** The reader interested in the private, trustless, zero-knowledge cloud will find the real discussion in the documentation of CloudServer and in the broader literature on cryptography, data sovereignty, and the failures of the public cloud exposed by the great data scandal. The lesson --- that a cloud you must trust is not a place to keep your future --- is one worth carrying well beyond the factory.

**On agents and their safety.** The reader drawn to the agentic side of the sixth revolution will want to study AgentBridge and its deterministic memory and sandbox, and the wider literature on constrained, self-hosted agents. The safety argument --- that an agent should be bounded by structure, not by prompt discipline --- is one that will matter increasingly as agents take on more real work.

## The Honest Caveat

This appendix points to real, published projects and to directions of further reading; it does not promise that any of them will be finished, stable, or easy. The lab's projects are live and evolving; links and details may change. The honest reader treats this appendix as a compass rather than a fixed map --- a direction to steer by, verified against the sources themselves. That, in the end, is the whole lesson of the sixth revolution: do not merely trust the book; go and read the sources, test the machines, and decide for yourself. The factory that thinks is not a promise to be believed; it is a practice to be examined.

