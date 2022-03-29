from flask import Flask, Response, url_for
app = Flask(__name__)


@app.route('/')
def home_page():
    about_us = url_for('about_us')
    return """
<html>
    <head>
        <title>Home</title>
        <style>

            body 
            {{
            background-color:#FCEADE;
            }}
            
            div 
            {{
            padding:25px 50px; background-color: 25CED1;
            }}
            
            .main_heading 
            {{
            style=border-style: solid; border-top-color: coral;
            }}
            
            h1 
            {{
            font-family: lucida handwriting; font-size:200%; color: #EA526F;text-align: center; 
            }}
            
            p 
            {{
            font-family: arial; font-size:100%
            }}
            
            section 
            {{
            padding: 25px 90px 25px 90px;
            }}
            
            .button 
            {{
            background-color: #336699;
            border: 10px solid #EA526F;
            color: FCEADE;
            padding: 5px 10px;
            text-align: center;
            display: inline-block;
            font-size: 20px;
            margin: 10px 30px;
            cursor: pointer;
            }}
        </style>
    </head>

    <section>
        <body>
            <div class="main_heading"> 
            <h1>Gaby and Salima's Home Page</h1>
            </div>
    
        <br>
        <br>
        <a href="{}"><button style= "display: block; margin: 0 auto;" class="button">About Us</button></a>
        
        <h2>Hello World</h2>

        <p>Nothing's gonna make your husband or wife madder than coming home and having a snow-covered dinner. Let the paint work. Now it's beginning to make a little sense. This is your world. I spend a lot of time walking around in the woods and talking to trees, and squirrels, and little rabbits and stuff.
        </p>

        <p>This is the time to get out all your flustrations, much better than kicking the dog around the house or taking it out on your spouse. We don't want to set these clouds on fire. We can always carry this a step further. There's really no end to this. Isn't that fantastic that you can create an almighty tree that fast? This is truly an almighty mountain.
        </p>

        <p>You need the dark in order to show the light. Let that brush dance around there and play. We wash our brush with odorless thinner. The very fact that you're aware of suffering is enough reason to be overjoyed that you're alive and can experience it. Van Dyke Brown is a very nice brown, it's almost like a chocolate brown.
        </p>

        <p>Trees get lonely too, so we'll give him a little friend. So often we avoid running water, and running water is a lot of fun. Just make little strokes like that. There is immense joy in just watching - watching all the little creatures in nature. Everyone needs a friend. Friends are the most valuable things in the world. Don't be bashful drop me a line.
        </p>
        
        <h2>Hobbies</h2>
        
        <p>You're the greatest thing that has ever been or ever will be. You're special. You're so very special. And that's when it becomes fun - you don't have to spend your time thinking about what's happening - you just let it happen. Don't be afraid to make these big decisions. Once you start, they sort of just make themselves. We spend so much of our life looking - but never seeing. Trees grow in all kinds of ways. They're not all perfectly straight. Not every limb is perfect. This is where you take out all your hostilities and frustrations. It's better than kicking the puppy dog around and all that so.
        </p>

        <p>You can spend all day playing with mountains. We're not trying to teach you a thing to copy. We're just here to teach you a technique, then let you loose into the world. These trees are so much fun. I get started on them and I have a hard time stopping. The only thing worse than yellow snow is green snow. This is probably the greatest thing that's ever happened in my life. Only think about one thing at a time. Don't get greedy.
        </p>

        <p>Now then, let's play. You don't want to kill all your dark areas they are very important. Use what happens naturally, don't fight it. We might as well make some Almighty mountains today as well, what the heck. Just think about these things in your mind - then bring them into your world. Anything you want to do you can do here.
        </p>
        
        <h2>Interesting fact</h2>
        
        <p>Maybe there was an old trapper that lived out here and maybe one day he went to check his beaver traps, and maybe he fell into the river and drowned. Brown is such a nice color. A happy cloud. Let's put some highlights on these little trees. The sun wouldn't forget them. Don't fight it, use what happens.
        </p>

        <p>Play with the angles. Just a happy little shadow that lives in there. There we go. We'll put all the little clouds in and let them dance around and have fun. The more we do this - the more it will do good things to our heart.
        </p>

        <p>Get away from those little Christmas tree things we used to make in school. Let your heart be your guide. Here's something that's fun. I'm a water fanatic. I love water. If what you're doing doesn't make you happy - you're doing the wrong thing. The man who does the best job is the one who is happy at his job.
        /p>

        </body>
    </section>
</html>
""".format(about_us)

@app.route('/about')
def about_us():
    home_page = url_for('home_page')
    return """
<html>
    <head>
        <title>About Us</title>
        <style>
            body 
            {{
            background-color:FCEADE;
            }}
            
            div 
            {{
            padding:25px 50px; background-color: 25CED1;
            }}
            
            .main_heading {{
            style=border-style: solid; border-top-color: coral;
            }}
            
            h1 {{
            font-family: lucida handwriting; font-size:200%; color: EA526F; text-align: center;
            }}
            
            p 
            {{
            font-family: arial; font-size:100%
            }}
            
            table 
            {{
            width: 50%; height: 25%; border: 15px solid #FF8A5B; 
            }}
            
            tr, th, td {{
            border: 3px solid #EA526F;
            }}
            
            td, tr 
            {{ text-align: center; vertical-align: middle;
            }}
            
            .center 
            {{
            margin-left: auto; margin-right: auto;
            }}
            
            section 
            {{
            padding: 25px 90px 25px 90px;
            }}

            .button 
            {{
            background-color: #336699;
            border: 10px solid #EA526F;
            color: FCEADE;
            padding: 5px 10px;
            text-align: center;
            display: inline-block;
            font-size: 20px;
            margin: 10px 30px;
            cursor: pointer;
            }}
        </style>
    </head>
    
    <section>
        <body>
            <div class="main heading">
            <h1>About Us</h1>
            </div>

            <br>
            <br>
        
            <a href="{}"><button style= "display: block; margin: 0 auto;" class="button">Home Page</button></a>
        
            <br>
            <br>
        
            <table class="center">
                <tr>
                    <th>About Us</th>
                    <th>Favourite Animal</th>
                    <th>Favourite Hobby</th>
                </tr>
            
                <tr>
                    <td>Gaby</td>
                    <td>Panda</td>
                    <td>Painting</td>
                </tr>
            
                <tr>
                    <td>Salima</td>
                    <td>Horse</td>
                    <td>Cycling</td>
                </tr>
            
            </table>

            <h2>Favourite Hobbies</h2>
        
            <p>Well, the way they make shows is, they make one show. That show's called a pilot. Then they show that show to the people who make shows, and on the strength of that one show they decide if they're going to make more shows. Some pilots get picked and become television programs. Some don't, become nothing. She starred in one of the ones that became nothing. 
            </p>

            <p>You think water moves fast? You should see ice. It moves like it has a mind. Like it knows it killed the world once and got a taste for murder. After the avalanche, it took us a week to climb out. Now, I don't know exactly when we turned on each other, but I know that seven of us survived the slide... and only five made it out. Now we took an oath, that I'm breaking now. We said we'd say it was the snow that killed the other two, but it wasn't. Nature is lethal but it doesn't hold a candle to man. 
            </p>

            <p>Well, the way they make shows is, they make one show. That show's called a pilot. Then they show that show to the people who make shows, and on the strength of that one show they decide if they're going to make more shows. Some pilots get picked and become television programs. Some don't, become nothing. She starred in one of the ones that became nothing. 
            </p>

            <p>Now that we know who you are, I know who I am. I'm not a mistake! It all makes sense! In a comic, you know how you can tell who the arch-villain's going to be? He's the exact opposite of the hero. And most times they're friends, like you and me! I should've known way back when... You know why, David? Because of the kids. They called me Mr Glass. 
            </p>
        
            <h2>Travelling</h2>
        
            <p>Your bones don't break, mine do. That's clear. Your cells react to bacteria and viruses differently than mine. You don't get sick, I do. That's also clear. But for some reason, you and I react the exact same way to water. We swallow it too fast, we choke. We get some in our lungs, we drown. However unreal it may seem, we are connected, you and I. We're on the same curve, just on opposite ends. 
            </p>

            <p>Well, the way they make shows is, they make one show. That show's called a pilot. Then they show that show to the people who make shows, and on the strength of that one show they decide if they're going to make more shows. Some pilots get picked and become television programs. Some don't, become nothing. She starred in one of the ones that became nothing.
            </p>

            <p>Now that we know who you are, I know who I am. I'm not a mistake! It all makes sense! In a comic, you know how you can tell who the arch-villain's going to be? He's the exact opposite of the hero. And most times they're friends, like you and me! I should've known way back when... You know why, David? Because of the kids. They called me Mr Glass.
            </p>

            <p>Now that there is the Tec-9, a crappy spray gun from South Miami. This gun is advertised as the most popular gun in American crime. Do you believe that shit? It actually says that in the little book that comes with it: the most popular gun in American crime. Like they're actually proud of that shit.  
            </p>
        
            <h2>Flying</h2>
        
            <p>You think water moves fast? You should see ice. It moves like it has a mind. Like it knows it killed the world once and got a taste for murder. After the avalanche, it took us a week to climb out. Now, I don't know exactly when we turned on each other, but I know that seven of us survived the slide... and only five made it out. Now we took an oath, that I'm breaking now. We said we'd say it was the snow that killed the other two, but it wasn't. Nature is lethal but it doesn't hold a candle to man. 
            </p>

            <p>The path of the righteous man is beset on all sides by the iniquities of the selfish and the tyranny of evil men. Blessed is he who, in the name of charity and good will, shepherds the weak through the valley of darkness, for he is truly his brother's keeper and the finder of lost children. And I will strike down upon thee with great vengeance and furious anger those who would attempt to poison and destroy My brothers. And you will know My name is the Lord when I lay My vengeance upon thee.
            </p>

        </body>
    </section>
</html>
""".format(home_page)


if __name__ =="__main__":
    app.run(debug=True)

