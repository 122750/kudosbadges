# kudosbadges

This repository contains the Kudos artwork that what is shown on the [Gitcoin Kudos marketplace](https://gitcoin.co/kudos)

## Why

Kudos are a recurring revenue stream for artists.

## What 

Kudos is a [non-fungible token](https://en.wikipedia.org/wiki/Non-fungible_token) that is created on the [Ethereum](https://www.ethereum.org/) blockchain, and can be sold to the [Gitcoin Kudos marketplace](https://gitcoin.co/kudos).  

# For Funders

Want your own Kudos?

Here's what to do: 
1. Open up a Github Issue [here](https://github.com/gitcoinco/kudosbadges/issues/new).
2. Fill out the template.
3. Pay for the kudos art.
4. We will mint the kudos.
5. You've got a branded kudos!

## For Artists:

### Compensation

There are two options for compensation for Kudos:

1. *Self Sovereign* - When a new Kudos is created, the ETH sent during that minting process is directly sent to the illustrator who created the Kudos artwork. In some cases, Gitcoin may also take a 10% fee to help keep the lights on.
1. *Gitcoin-Funded* - Gitcoin will pay you for each piece of artwork, and will collect the self sovereign (#1) funds.  [Email us](mailto:founders@gitcoin.co) a link to your portfolio to be considered.

Right now, we expect that most ppl will want to do Gitcoin-Funded kudos art. But down the line, when people are making $100s per day off their Kudos art, we hope people will consider the self sovereign route.


## to create a new Kudos

0. Kudos must be ORIGINAL art or art you own the liscense to.  If you are creating a Gitcoin-funded kudos, [email us](mailto:founders@gitcoin.co) to negotiate a rate for your artwork.  Please include your portfolio link.  If you are going the Self Sovereign route, skip this step and proceed to next step.
1. Checkout the latest [kudos design guide](https://github.com/gitcoinco/creative/blob/master/Product/kudos_guide/kudosguide_latest.pdf).
2. Checkout the latest [ideas for kudos](https://github.com/gitcoinco/kudosbadges/projects/1).
3. [Open up a PR against this repo](https://help.github.com/articles/creating-a-pull-request-from-a-fork/) with your proposed artwork in it.

# Dev Stuff

## Naming schema

For consistency, name all images with all lowercase letters and underscores between each word.  For example,

- level_up.svg
- night_owl.svg

## kudos.yaml file

This file contains the information about each of the kudos artifacts.  When adding a new Kudos, please add a corresponding record to the file.

## init_kudos.py

This python script reads the **images** directory and creates a kudos.yaml file.  It uses the filename to create the `name`, the `image` field.  The rest of the fields are sample defaults.

You only need to run this script if the kudos.yaml file doesn't already exist.

## See also

[Kudos721Contract Repo](https://github.com/gitcoinco/Kudos721Contract)



# License

[LICENSE](../LICENSE)

<!-- Google Analytics -->
<img src='https://ga-beacon.appspot.com/UA-102304388-1/gitcoinco/kudosbadges' style='width:1px; height:1px;' >
