# open-elecbay
Inspired by 'elecbay' a distributed energy marketplace solution

## Dependencies
Docker, see this page for installing Docker Desktop.


## Getting Started

### From DockerCompose

Must have Docker-Compose on the machine. From the root of the repo run this command.

```
docker-compose up
```

### From DockerFile

Build the image in docker.

```
docker build -t open-elecbay .
```

Run the following docker build command at the root of the repo.

```
docker run -dp 5000:5000 open-elecbay
```


## Usage

Environment loads mosquito MQTT broker locally on the docker app. 
Messages are received through the frontend API , and forwarded to the MQTT broker.
The MQTT broker is then serviced by a market agent that supervises the bidding, exchange, and settlement periods
A different market agent can be designed to independently manage each of these periods.

A participant can then register through the API and then stream requests to the MQTT broker for any of the periods
Participants can publish/subscribe requests based on a participant ID/key provided by the API after registration



# Software Design

Use of MQTT Broker
- A Publish/Subscribe protocol for IoT 
- Used to replicate an exchange market
- Used to handle multiple topics so that "bots" could interact

Topics:
- HourlyMarketState:
    - What Publishing cycle we are on?
        - Gate Closure for that publshing cycle , for a given bidding period
    - Whate energy exchange cylce are we on?
        - when does this energy echange time end?
    - What hour is currently settling?
        - when was the bill date for this?
        - what exchange hour is settling
        - what bids for this settlement?

- Orders:
    - can be placed cancelled and modified by peers only before the gate closure
    - orders are tied to a bidding period (when submitted)

- ItemList : 
    - offers of available generation with "start" duration, and amount from sellers
    - typically surplus energy over half an hour for sale


The generation and consumption of the bots should be dependent on a global trend and then updated as needed for each bots particular consumption or generation limitations.

- SolarOutput : 
    - provides changes of irridiance for bots 
    - also provides forecast for future changes?

- TypicalConsumptionCurve:
    - a topic with base consumption curve for every hour

Model of the Supplier
- Generation source (PV)
    - would need some kind of trend of what is generated
    - requires a connection to an atomic clock counter
    - could also reference a topic for irridiance


bots.. can be crreated on seperate threads
elecbay needs to process orders that it recieves.
return the order post with "accepted/rejected"

bots can now order from elecbay

elecbay needs to have a sequence that changes
between states?

also the bots need to be synchronized with the elecbay

can i build a topic that has a timer?
should elecbay just coordinate? with its own internal timer?

build a publish topic so buyers can browse available items to purchase?


# How it works

The appcontainer needs to spin up in order to host the broker.

1. Create a request to the market using the /request endpoint
2. Recieved an ID from the created request then submit it to the market
3. 


I need to post requests simpler so that i can place the broker/agent logic


# Get Started

1. Navigate to the API on http://localhost:5001/swagger/ 
2. Request a new market request

## Mosquito MQTT Broker
The Mosquito MQTT Broker is a free open source MQTT Broker that runs on the local machine.
The container for the MQTT Broker is called 'mosquitto'. Logs from the container are shown below after startup of the broker.

```
1636720700: mosquitto version 2.0.11 starting
1636720700: Config loaded from /etc/mosquitto/mosquitto.conf.
1636720700: Opening ipv4 listen socket on port 1883.
1636720700: Opening ipv6 listen socket on port 1883.
```

Connection from the agent to the broker is shown below.
```
1636720700: mosquitto version 2.0.11 running
1636720700: New connection from 172.18.0.3:58175 on port 1883.
1636720700: New client connected from 172.18.0.3:58175 as agent1 (p2, c1, k60).
1636720701: New connection from 172.18.0.4:35695 on port 1883.
1636720701: New client connected from 172.18.0.4:35695 as auto-CD05CD69-A62C-3E65-EE15-353D83E4C6B2 (p2, 1636728801: Client agent1 closed its connection.
1636729219: New connection from 172.18.0.3:55207 on port 1883.
1636729219: New client connected from 172.18.0.3:55207 as agent1 (p2, c1, k60).
1636729393: New connection from 172.18.0.3:36777 on port 1883.
1636729393: Client agent1 already connected, closing old connection.
1636729393: New client connected from 172.18.0.3:36777 as agent1 (p2, c1, k60).
1636729484: Client agent1 has exceeded timeout, disconnecting.
```

Connection from filebeat to the broker is shown below.
```
1636720702: New connection from 172.18.0.8:56420 on port 1883.
1636720702: New client connected from 172.18.0.8:56420 as filebeat (p2, c1, k30).
```



# Acknowledgements

[1] Sean Bradley's swagger example was used to standup the web and API layers using REST Python Flask Server.(https://github.com/Sean-Bradley/Seans-Python3-Flask-Rest-Boilerplate)

# References

[1] Mediwaththe Gedara Chathurika Prasadini Mediwaththe ; "Game-theoretic Methods for Small-scale Demand-side Management in Smart Grid"  A thesis in fulfillment of the requirements for the degree of Doctor of Philosophy School of Electrical Engineering and Telecommunications Faculty of Engineering, The University of New South Wales Australia January 2017

[2] Andrew McEachern; "Game TheoryA Classical Introduction, Mathematical Games,and the Tournament", Queen’s University, SYNTHESIS LECTURES ON GAMES AND COMPUTATIONALINTELLIGENCE #1, claypool Morgan publishers;  Morgan & Claypool 2017

[3] LEFENG CHENG , (Student Member, IEEE), AND TAO YU , (Member, IEEE), Game-Theoretic Approaches Applied to Transactions in the Open and Ever-Growing Electricity Markets From the Perspective of Power Demand Response: An Overview ; Received February 3, 2019, accepted February 17, 2019, date of publication February 21, 2019, date of current version March 8, 2019.

[4] He Zhang, Yuelong Su, Lihui Peng, Danya Yao Member, IEEE; A Review of Game Theory Applications in Transportation Analysis ; International Conference on Computer and Information ApplicationICCIA 2010152C978-1-4244-8598-7 /10/$26.00 2010

[5] Tamer Ba ̧sar ; Lecture Notes on Non-Cooperative Game Theory; July 26, 2010
  
[6] Wayes Tushar, Student Member, IEEE, Walid Saad, Member, IEEE, H. Vincent Poor, Fellow, IEEE,andDavid B. Smith, Member, IEEE; Economics of Electric Vehicle Charging: A GameTheoretic Approach, IEEE TRANSACTIONS ON SMART GRID, VOL. 3, NO. 4, DECEMBER 2012

[7] B. Tolwinski, “A Stackelberg solution of dynamic games,”IEEE Trans.Autom. Control, vol. AC-28, pp. 85–93, 1983

[8] LEFENG CHENG , (Student Member, IEEE), AND TAO YU , (Member, IEEE), Game-Theoretic Approaches Applied to Transactions in the Open and Ever-Growing Electricity Markets From the Perspective of Power Demand Response: An Overview ; Received February 3, 2019, accepted February 17, 2019, date of publication February 21, 2019, date of current version March 8, 2019.

[9] L. F. Cheng and T. Yu, ‘‘Nash equilibrium-based asymptotic stability anal-ysis of multi-group asymmetric evolutionary games in typical scenario ofelectricity market,’’IEEE Access, vol. 6, pp. 32064–32086, Dec. 2018.doi: 10.1109/ACCESS.2018.2842469.
  
[10] J. von Neumann and O. Morgenstern,Theory of Games and EconomicBehavior. Princeton, NJ, USA: Princeton Univ. Press, 1944.

[11] J. F. Nash, Jr., ‘‘The bargaining problem,’’Econometrica, vol. 18, no. 2,pp. 155–162, 1950.

[12] J. F. Nash, Jr., ‘‘Equilibrium points in n-person games,’’Proc. Nat. Acad.Sci. USA, vol. 36, no. 1, pp. 48–49, 1950.

[13] J. Nash, ‘‘Non-cooperative games,’’Ann. Math., vol. 54, no. 2,pp. 286–295, 1951.

[14] J. Nash, Jr., ‘‘Two-person cooperative games,’’Econometrica, vol. 21,no. 1, pp. 128–140, Feb. 1953. doi:10.2307/1906951.

[15] J. M. Smith and G. R. Price, ‘‘The logic of animal conflict,’’Nature,vol. 246, no. 5427, pp. 15–18, Jan. 1973. doi:10.1038/246015a0.

[16] P. D. Taylor and L. B. Jonker, ‘‘Evolutionary stable strategies and gamedynamics,’’Math. Biosci., vol. 40, nos. 1–2, pp. 145–156, Jul. 1978.doi: 10.1016/0025-5564(78)90077-9.

[17] L. F. Cheng and T. Yu, ‘‘Exploration and exploitation of new knowledgeemergence to improve the collective intelligent decision-making levelof Web-of-cells with cyber-physical-social systems based on complexnetwork modeling,’’IEEE Access, vol. 6, pp. 74204–74239, Oct. 2018.doi: 10.1109/ACCESS.2018.2879025.

[18] Wang, Min, "Mathematical and statistical models in evolutionary game theory" (2015). Graduate Theses and Dissertations. 14449.
https://lib.dr.iastate.edu/etd/14449


[19] Blackwell  and  Girshick, "Games  in  Normal  Form";  pp.  1-24  in Theory  of  Games and Statistical Decisions.Wiley publications in statistics, New York, 1954.