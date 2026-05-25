+++
title = "What does a customer mean whey they say your software is \"noisy\"?"
date = 2023-08-17
lastmod = 2023-08-17
+++

I have worked in/with security software since about 1996.  I have talked to hundreds or thousands of customers/users of security software over the years.  One of the things that I hear people say frequently about security software is that it's "noisy".   This observation is usually targeted at time series output like logs and so forth.

After diving deep on a lot of these issues to understand what people meant by that, I've come up with a simple taxonomy describing what "noisy" means from the customer's point of view.  The purpose of this taxonomy is to help security (or other) software developers avoid or fix problems with their output in order to delight their customers, or at least not disappoint them.

To spoil the surprise, "noisy" effectively inversely correlates with "actionable".

Basically, when a customer says something is "noisy", they usually mean one of the following:

- **Volume** - "There is way too much output; I'm overwhelmed by the volume"
- **Understandability** - "I don't understand this output, therefore it is not actionable by me"
- **Actionability** - "I understand the output, but it is not actionable by me"
- **Redundancy** - "I understand the output, and it is actionable, but it has a lot of redundancy and multiple outputs map to the same action by me"
- **Relevancy** - "I understand the output, and it may be actionable, but it is not relevant to me"

So some useful things to do to avoid and/or solve these kinds of issues are:

1. If there is too much output for one person, consider changing the output from time-series or interrupt-based (e.g. notifications), to periodic reports.
2. Make your output clear and understandable to a layperson who doesn't write software, let alone your specific software.  Note that good reports require prioritization.
3. Make sure that your output unambiguously points to a remediation action to be taken by a human.
4. Try to aggregate your output such that there is a 1:1 mapping between the output and the action to be taken by the human.  For instance, if you have the same security vulnerability on all instances of a homogenous fleet, generate one output (for the fleet) that points to the "best" remediation action ("fix the image and redeploy"), rather than generate an output for each fleet member.
5. Build your software so that the user only gets output that they care about - that means building a way for the user to tell you what the do (and don't) care about.  This might take the form of a policy UI for what kinds of output to generate, or might take the form of a simple way to suppress future instances of output they don't care about.

Note that busy people generally just want a list of "what do I need to do today and what should I do first?".  Any dashboarding or reporting solution that you build for your security information should keep that in mind.   The ideal is a prioritized list, with the most important thing at the top, and then other things in order of descending priority.

Note that priority is not exactly the same thing as "severity".  A single change that eliminates 100 high severity risks might be more impactful than a single critical risk.  In human terms, "priority" combines concepts of severity, impact, and actionability.

I hope this helps you build better software.  Lots of developers I've worked with have pushed back on these kinds of issues, not feeling that it is important.  However you often don't get a second chance to make a good impression, and if your software doesn't behave in accordance with user expectations they have a tendency to turn it off and/or ignore it.

Eric

- [ed] 2024-01-29 to add more information on prioritization
- [ed] 2024-07-16 added taxonomic labels
