+++
title = "What if there were a cryptocurrency that supported disputes?"
date = 2023-01-14
+++

I'm just jotting down a random idea here; maybe it's not fully formed yet.

I think that there are two main reasons that normal people eschew cryptocurrency:  
1. Transactions are irreversible and indisputable.  Once the transaction is signed and confirmed, the crypto is gone forever.  
2. Normal humans just aren't cut out to protect secret keys well, and one misstep can result in either exposing your key (see #1) or in losing your key; either way you just lost all the cryptocurrency in your wallet, forever.  

Dorsey et al are working on solutions to #2 [Block hardware wallet](https://www.protocol.com/bulletins/block-bitcoin-hardware-wallet).  But I'm thinking about #1.

What if there was a cryptocurrency that supported the ability to adjudicate disputes and reverse transactions?

I'm thinking of something like bitcoin or Ethereum, but with "adjudicator" keys.  Adjudicator in this sense means "someone trusted to resolve disputes", which might be a court or might be someone/something else.

The idea is that courts or other entities could generate such key pairs, and publish them in some fashion (e.g. in their dockets?).  The keys would have to be attested to on the blockchain, perhaps as just a transaction of a specific type.  Similarly, self-revocation or community revocation via a transaction could occur in the same manner should the adjudicator key be misused.

Now the interesting thing about an adjudicator key is that it can be used in two ways:  
1. The key can be used to make a new transaction that reverses an earlier transaction.  
2. The key can be used to make an assertion about an existing transaction, to the effect that the transaction is in dispute and subject to adjudication.   This obviously needs a resolution assertion as well.  

The idea is that if A transfers crypto to B in exchange for a good or service, but then wants to dispute the outcome, that they work with an adjudicator J asap to post a dispute, ideally preventing B from moving all their crypto out of that wallet in an attempt to evade reversal.  By "prevent" I mean that other participants in the blockchain would be hesitant to receive crypto from B because of the pending dispute and possibility for reversal.  The dispute assertion is advisory, not compulsory.

At some point later, J adjudicates the dispute and either posts a reversal of the original transaction, or posts a "no longer in dispute" transaction.

Yes there are risks involved.  What if bad people get control of an adjudicator key?  What if government actors get an adjudicator key and starts using it to "sanction" people?  Would such keys enable involuntary taxation?  What happens if you reverse a transaction but the crypto has branched out from the original wallet?  I freely admit there are lots of problems here.

I dunno.  But I will say that the idea that I could go to court and undo the transaction where the bad guy stole all my crypto, makes me a lot less nervous about it.
