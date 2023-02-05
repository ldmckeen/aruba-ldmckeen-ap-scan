# Documented Notes for Aruba Reviewers

Below is a brief outline of some items for the Aruba team Reviewing:
### Caveats
While many simpler API frameworks could have been used or just straight python
implementation without a framework, I chose to utilise Django Rest Framework as the
tool of choice for this application for a few reasons.
1. DRF comes with some great and easy to use classes and views for simple API setup,
and implements a great MVC (Model View Control) or MVT to be more specific (Model View
Template) architecture, making model setup and integration with a database simple and easy
to use put of the box.
2. DRF makes it easy to have a user authentication system built in, and with some simple
configuration you can ensure interaction with your API's is secure.
3. With DRF creating the views is easy and the developer can focus on logic and implementation.
4. I have experience familiarity with Django when designing API's

While there isn't necessarily a need for models and a database, I added in some classes and
object functionality for future features to be easily implemented if the API and application
wer to be expanded upon.

Other files in repo for git ignores, pep8 checks, per-commits etc are standard files for
good git practices I've used previously, these are common to many of the repos I use on a
daily basis, so I’ve referenced those and implemented them on this repo as well.

*Comment on the comments:* Normally I would not write as many comments file header summaries
and descriptions in the files themselves as ideally the code should be readable and intuitive
enough to derive meaning, context and logic flow from the code itself, but again for the sake
of ‘demo’ purposes in this case it was just for an in depth showcase of the solution to the
problem statement presented and tasked.

Any further info please don’t hesitate to reach out to me.
I can disclaim this code was written entirely by myself (albeit with some references to online
python resources and stack overflow for some non in-brain-memory syntax's and library
functions etc. :-P

### Troubleshooting

## *Pending Improvements and Future Updates .....*
### Application Updates:
* Update API to store result data for future reference and analytics.
* Make use of the APScanData classes and object store for storing rows of data, update with
functions and methods to further enhance interaction with the Geolocate and other external
helpful API's regarding sensor data.

#### Coding Updates:
* More Detailed Doc String Params
* Type hints
* Update Exception handling to exit more gracefully and send raise errors to the console where applicable.
* Update logging to output to log files and std out with single logging code statements
* Add swagger for prettier and more functional frontend API capabilities.

#### System Updates
* Update to make use of a choice of DB instances.

#### DeploymentUpdates
* Dockerise Application for use in a containerised environment
* Add deployment scripts to spin application up on a simple VM in the cloud
* Add GitHub checks and analysers to analyse code and run unit tests and analysis on code according to best practices and coding standards
