# Smart-Breathalyzer-using-Tkinter

A breathalyser, often known as a Breathalyser, is a device that measures blood alcohol content (BAC) from a breath sample. This little project sample code calculates the BAC level using randomised input values and determines whether it is within the legal driving limit. Actual values can be extracted from a real device and integrated into the programming. If the BAC level exceeds the legal limit, the device will have choices for cab booking and calling emergency contacts by pairing with the mobile, which can be coupled with APIs in the future and the same interface can be built as a mobile app with alternative software. The smartphone app can be coupled with the vehicle to start the engine and maintain a speed limit.

Algorithm:

1. Start
2. Request a blow for examination.
3. If the BAC level is 0, then the person is not drunk.
4. If the BAC level lies between 0 and 0.05, then it’s within the legal limit to drive.
5. If the BAC level is between 0.05 and 0.08, then it’s within the legal limit for driving, but it asks whether the user wants to book a cab or call home for safety.
6. If the BAC is > 0.08, then display that it’s illegal to drive and ask.
  • Whether or not to book a cab with the pre-programmed address
  • Whether or not to contact a family member
  • Whether it’s an emergency to start the vehicle and ask 
    a. If the user has someone to drive them home.
    b. Otherwise, start the vehicle and limit the speed to 40 km/hr. 
7. Stop.
