


# Overview of the Electric Grid 
 

The conventional electric grid is comprised of central power stations generating electricity and then leveraging transformers to increase the voltage before sending it long distance over a nationwide transmission line system. The energy arrives at the consumers distribution network then is stepped down to lower voltage levels that are safer to travel over the local distribution lines and into the drop of a consumer’s meter before arriving and powering the connected loads of the home or building. 

Suppliers secure energy from the generating sites for their own consumers. The flow of electricity and the flow of information are both unidirectional and travel in opposing directions. The suppliers need to know the real-time demand of electricity by consumers to secure generation of electricity for that demand. The conditional factors such as the variability of the demand and generation are considered as well as the losses moving the energy across transmission and distribution networks. The balancing of electricity is required because conventionally the capability to store energy in any significant way was not available. As of 2021 the energy storage capabilities are still not capable of significantly displacing enough energy forego the real-time balancing challenges. 

The conventional Grid was designed to efficiently leverage the high inertia energy generating systems such as fossil fuels heating water and moving steam through fan blades in the form of a turbine. The spinning turbines armatures rotate permanent magnets through coils to generate electricity through the periodic flux of collapsing electro-magnetic fields. These rotating systems form a current on wires that alternates from positive and negative coordinated with the rate of rotation. The frequency that the current alternates has been standardized in North America to remain as close to 60 cycles per second as possible. The alternating current (AC) three similar currents from three different generating systems can all be tied to the same returns line. There is also another special property where that return line can be removed if each wave is synchronized to be out of phase with the other two. The 3-phased AC transmission system can provide efficient transfer of high voltage electricity across large distances. 

 

## Growth of the Grid 

The consumption of energy by consumers has traditionally been predicted by the suppliers based on a general load curve of a typical home. The major components of the typical home have been air conditioning, water heaters, and lighting. These systems have been getting increasingly efficient over the years. The utilities that supply energy to these consumers has also enacted incentives for off-peak hour usage of electricity. The variable rates for the energy usage were an attempt to shift the user into adopting psychologically different habits that could shift the load curve of a home when generation is not available. 

Renewable energy sources where traditionally only available in places that provided a geographical advantage such as damns, rivers, and waterfalls. These hydro-electric sources where dependable and always available even during a “black out”. Since conventional turbines generators required substantial amounts of reactive power to energize the large coils before producing any electrical output these systems required energy from the Grid to get started. Renewable resources like a hydro-electric power plant would not need any energizing energy and could produce enough energy to black-start other generators on the Grid. Renewables that depend on dynamic sources such as wind or solar where not as efficient as hydro for a long time.  

A combination of wind turbine technology, originally pioneered by European countries at a large scale, and the changes in policy during the late 1960’s created a surge of wind turbine based powerplants in areas through-out North America that could sustain large winds. Valleys and corridors in the west and mid-west regions would develop many wind sites under the PURPA law of 1967. Companies like Enron would invest heavily in the technology to take advantage of energy tax credits provided by the government. In Great Britain, the wholesale market was created to allow suppliers to provide energy in 1990 to consumers by purchasing it for the consumers from generators. The “Pool” was used for compulsory day-ahead market for bulk physical trading. The Pool selling prices could also be manipulated by the major generators because it only had a couple major Generators. To create more fairness a bi-lateral trading mechanism was proposed that leverage a rolling gate closure.  

 

## Energy Market Overview 

The energy market consists of suppliers buying energy from generators to transmit it over powerlines to consumers. The research focuses on the Great Britain “Pool” day-ahead market but can also apply to other markets such as the regional markets in North America. The market requires the need for real-time exchange. The real-time exchange is required to balance the energy across the Grid to avoid blackouts or damage to the equipment. The balancing is done by a central authority that is also in charge of approving the final market transactions. The balancing authority has the power to make additional deals with suppliers and generators to request ancillary services such as reserved generation or flexibility in the consumption. The market is broken up into a bidding period, an exchange period, and a settlement period. 

 

## General Market Process Flow 

The market mechanics are going to have different steps based on what state the participant starts in, but the general ones are provided below. The participant is either 

Registering on to the market, 

Bidding/Offering before the gate closure (GC) 

Consuming/Generating energy within the energy exchange period, (where they can be asked to bid additionally for balancing service opportunities) 

 

Figure 1. 

 

1 Process flow of entering bids and exchanging on settled contracts over the market 

 

## Settlement Period Contracting 

Each settlement cycle consists of interactions between the producer, consumer, and broker. The current process uses a series of bids and offers that are negotiated between the producer and consumers resulting in approved contracts by the broker before the gate closure deadline is reached. The submitted contracts are monitored so that any deviation results in the appropriate fiscal impact as indicated by the balancing authority. The broker also assesses the imbalance and looks for additional negotiations with the parties to amend the contracts as needed to help the imbalance. 

 

Figure 2. 

Feedback: This flowchart, is not simple enough to present the concepts. Break this up in order to educate the reader . Focus on the components that we are going to improve.  


Relate this to the blockchain distributions and to the physical network  

## Manage the Imbalance 

There is often a disparity between the promised amount of energy in the placed orders and the actual energy consumption as recorded by smart meters. After the settlement process the broker needs to find ways to settle the imbalance. It does so by leveraging different mechanisms during the energy exchange period. 

 

Feedback : Create a simpler concept for this flowchart. What is the balancing supposed to do. Try to copy the graph in the paper to show the timeline, but you would need to replicate it 

## Balancing Services Adjustment Data 

Alongside the Billing Mechanism the Balancing Services are additional bids that are taken from the committed participants to help balance out the grid. The additional offers/bids are done through an auction style system where the broker chooses the best possible solution for the imbalance effort required factoring in safety, time, and price into the equation. 


## Billing Mechanism 

After the gate closure for the settlement period. The Billing Mechanism (BM) is used to evaluate the net imbalance of the transmission system. 

 

## Appendix 

Peer to Peer Trading: The paper covers the design of the Great Britain Electric Grid. The transactions between the generators and consumers are managed by "Peer-to-Peer" (P2P) Energy Training 

Market Architecture: A hierarchal system architecture is modeled and proposed to identify and categorize key elements and technologies involved in P2P energy trading. The bidding is simulated using Game Theory to test the transactional mechanisms of the market. 

Grid Architecture: A grid-connected Low Voltage (LV) Microgrid is tested, containing distributed generators and flexible demands. The test results indicate an improvement to the local balance of energy generation and consumption correlated with the variety of peers able to further facilitate the balance. 

Proposed Control Systems: The paper proposes two necessary control systems for the Microgrid. A voltage control system with droop control and on-load-tap-changer control. 

Network Architecture: The current information and communication technology infrastructure (ICT) is investigated and confirmed to be able to support the P2P energy trading platform. This utilizes the existing TCP/IP protocol designs. 

Software Architecture of Open-Elecbay: A proposal for an architecture that handles streaming IoT data sets from multiple clients requesting independent bids/offers on the market. The architecture utilizes MQTT and existing IOT protocol to facilitate a publish/subscribe style of communication. The transaction of the system is brokered and recorded through various microservices. The design can be scaled and distributed across agents. 

 


# Refrences:

[] Transforming Energy Networks via Peer-to-Peer Energy Trading,IEEE SIGNAL PROCESSING magazine, 2018


[] Peer-to-Peer Trading in Electricity Networks: An Overview , Wayes Tushar,Senior Member, IEEE,Tapan K. Saha,Fellow, IEEE,Chau Yuen,Senior Member, IEEE,DavidSmith,Member, IEEE,and H. Vincent Poor,Fellow, IEEE, arXiv:2001.06882v1  [cs.MA]  19 Jan 2020

[] Performance Optimization for Blockchain-Enabled Industrial Internetof Things (IIoT) Systems: A DeepReinforcement Learning ApproachMengting Liu,F.RichardYu, Fellow, IEEE, Yinglei Teng, Member, IEEE,Victor C. M. Leung, Fellow, IEEE, and Mei Song


[] Game-theoretic Methods forSmall-scale Demand-sideManagement in Smart GridMediwaththe Gedara Chathurika Prasadini Mediwaththe, thesis in fulfillment of the requirements for the degree of Doctor of Philosophy School of Electrical Engineering and Telecommunications Faculty of Engineering, The University of New South Wales Australia, January 2017