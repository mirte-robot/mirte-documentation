Mirte Development
#################

As mentioned before we zre currently still developing Mirte. But the ultimate goal is to have a vibrant
community contributing to the project.

.. warning::
   Currently none of the interfaces (hardware, software) are definitive. This means that we might still
   change this. Developing educational material around Mirte is possible, but you should be able to
   modify this in case we change the interfaces.


Software architecture
=====================

As the robot is meant for education, most of the design decisions we made were made with that in mind. This
means we were forced to make decisions in the speed vs usability (/learnability) tradeoff and decided to go
for the learnability over speed. We this improving speed should, at some point, be done by the students
themselves. 




Repository overview
===================

The source (code, hardware design, electronics design, tutorials, etc) are all hosted on github. The 


Building a custom SD image
==========================


Development for Web Interface
=============================


Adding another language
=======================

Multi langual support is only available in the web interface and tutorials. We think children should
learn technology in their own language instead of having to learn a foreign language at teh same time. 
At some point we do think students should be able to use English as a language to learn more about
techology. 

The main language is English and can be found the frontend_ code. Adding a language can be as simple 
as a pull request with another json file.

.. _frontend: https://github.com/mirte-robot/mirte-web-interface/vue-frontend/locale/en.json
