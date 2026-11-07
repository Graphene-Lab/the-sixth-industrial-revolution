
# Appendix A --- A Glossary of the New Language

## Why a Glossary

The sixth industrial revolution has, like every revolution, brought its own vocabulary --- words that were once the private property of engineers and programmers and have now, quietly, become part of the language of the factory and, in many cases, of the office. This appendix is a gentle guide to those words, defined in plain language the moment they are useful, but gathered here so that the reader can dip back into them at leisure. Nothing here requires a degree to read; each definition is written as if explaining to a thoughtful newcomer.

## The Terms

**Agentic AI.** An AI that does not merely answer a question but pursues a goal: it plans, acts, observes the result, and adjusts, using the tools it has been given. Unlike a chatbot that waits to be spoken to, an agent is handed an objective and figures out how to reach it. AgentBridge is an example.

**Assembly (software).** The compiled artifact a program produces when it is built --- the most detailed, exact, unambiguous specification of what the program does. In deterministic AI (see below), the assembly is used as the source of truth, rather than a natural-language prompt that must be interpreted.

**Cloud (public and private).** A public cloud is a set of giant data centers owned by a few companies, where you store and compute data that lives on someone else's machines. A private cloud is kept inside a single company's control. The sixth revolution favors the private, trustless, zero-knowledge cloud (see those terms).

**Deterministic AI.** AI --- or, more precisely, automated computation --- that produces the same, guaranteed result every time, with no guesswork. It is the mind of the compiler: exact, traceable, provable. It is ideal where a decision must be certain (safety, finance, compliance) rather than merely plausible.

**Edge AI / on-machine AI.** Intelligence that runs locally, on or near the machine that produces the data, rather than sending the data to a far-away cloud to be processed. It is faster, cheaper, and more private, because the data does not leave the building.

**NPU (Neural Processing Unit).** A small chip inside a larger processor, built specifically to run neural-network (machine-learning) models quickly and efficiently, especially locally. It is what lets a small card on a factory machine "see" and "predict" without a round trip to the cloud.

**SBC (Single-Board Computer).** A complete computer on a single circuit board. The modern intelligent SBCs are based on ARM processors with a built-in NPU, are often fanless, and can be very cheap --- which is what makes on-machine intelligence affordable to everyone.

**Telemetry.** Data measured at one place and reported, automatically and continuously, to another. On a factory it is the live stream --- vibration, temperature, current, sound, images --- that reports the machine's condition in real time. It is the blood of the new factory.

**Trustless cloud.** A cloud you do not have to *trust* to behave, because its architecture --- not the operator's good intentions --- keeps your data safe. Your data is encrypted with a key only you hold, so the cloud can process and sync it without ever being able to read it.

**Zero-knowledge cloud.** A cloud that can verify and process your data without ever learning the data itself. It operates on the locked safe, never on the contents. Named after "zero-knowledge proofs" in cryptography, which prove a statement is true without revealing anything beyond that truth.

**Digital twin.** A live, digital model of a physical thing --- a machine, a line, a whole plant --- that mirrors its real state. On the sixth revolution, a digital twin can live locally on the machine's own board, always available and private.

**Humanoid.** A robot that moves on two legs the way a human does, and therefore can use a world built for humans --- doors, stairs, levers at hand height. On the sixth revolution, the humanoid is valuable where the work is dangerous, inaccessible, or wears down the human body, rather than as a general replacement for every worker.

**Robotics / collaborative robotics (cobotics).** The science of machines that move and act. Collaborative robots are designed to work *beside* humans safely, constantly perceiving their surroundings and adjusting, rather than being caged off from people.

**LLM (Large Language Model).** A machine-learning model trained on enormous amounts of text to understand and generate human language. It is flexible and impressive, and it can make things up --- which is why, where certainty matters, it is combined with deterministic computation rather than trusted alone.

**PLC (Programmable Logic Controller).** The old, extraordinarily reliable controller on virtually every factory floor, which reads switches and sensors and turns outputs on and off by explicit human-written rules. The sixth revolution does not necessarily break the PLC; it augments it with a small intelligent card that perceives and predicts what the PLC never could.

**Vision / visual inspection.** Using a camera plus a learned model to judge products automatically --- spotting scratches, misalignments, defects --- at the speed of light and without the fatigue of a human eye.

**Predictive maintenance.** Predicting, from a machine's own signals (vibration, temperature, sound, current), when a part is about to fail, so repair can be scheduled before the failure rather than after it.

**Autopilot / the office at midnight.** The vision, explored in this book, in which an agent --- knowing the business and working within a private cloud --- finishes office work (accounting, warehouse, sales, support, compliance) automatically, continuously, and privately, so the office keeps working after the lights go out.

**Autopoiesis.** Literally "self-making" (from the Greek *auto*, "self," and *poiesis*, "production"). A term coined in 1972 by Humberto Maturana and Francisco Varela for living systems, which build and repair their own components without anyone assembling them from outside. The book uses it in an extended sense: an industrial system that designs its own tools, writes its own agents, and maintains its own clouds has made itself independent of the human being, who is left outside the cycle of reproduction.

**Industry 7.0.** The framing this book uses for the sixth revolution: the seventh generation of industry, in which machines become peripherals of an internal AI, and that AI --- agentic, connected to a private cloud, knowing the business --- automates the whole enterprise into one self-coordinating loop.

## The Honest Note

A glossary can give the false impression that these terms are fixed once and for all. They are not --- the language of the sixth revolution is being written as we speak, and some of these words will shift. Read this appendix as a friendly starting point, not as a verdict. The book that follows will define each term as it is needed, in context, because context is where words truly live.

