## Find That Data!
We're first presented with a typical login portal. If we go into the source, we see that we can login with the following information
```
if (username == "CLU" && password == "0222") {
          window.location = "/maze";
        } else window.location = "/";
```

We're then presented with a maze and some move buttons. We can change the javascript move functions to instantly get to the end.

```
function move_down() {
  let cell = get_cell(x, y + 1);
  if (cell == null) return;
  if (y == maxRows || cell.style.borderTopStyle != "hidden") return;
  remove_x();
  y += 43;
  add_x();
  check_data();
}

function move_left() {
  let cell = get_cell(x - 1, y);
  if (cell == null) return;
  if (x == 1 || cell.style.borderRightStyle != "hidden") return;
  remove_x();
  x -= 35;
  add_x();
  check_data();
}
```

Flag: `flag{you_aren't_making_me_talk!}`


## Programs Only
The first thing we see on this website is the banner that tells us what seems like certain browsers. Taking a look at the source, we notice that there's a commented out link to a page called programs. If we try to manually access it, we're told that "Users do not have access to this resource."

The name of the chal is "Progams Only." We change our user agent to "Program"
It gives us a new page, but not the flag. I then thought, hm, what if we check the robots.txt file? Aha! We're given this:

```
User-agent: *
Disallow: /

User-agent: Program
Allow: /program/

User-agent: Master Control Program 0000
Allow: /program/control
```
We change our user-agent to `Master Control Program 0000` and access the page at /program/control to get our flag.

Flag: `flag{who_programmed_you?}`


## Reindeer Flotilla
Source! In the JS file, we find a var with the comment "don't waste your time with this." Printing the variable to the console gives us the flag.
Flag: `flag{y0u_sh0uldnt_h4v3_c0m3_b4ck_flynn}`


## First Day Inspection
> It's your first day working at ENCOM, but they're asking you to figure things out yourself. What an onboarding process... take a look around and see what you can find. 
Search through devtools, not too hard to find.
Flag: `flag{w3lc0m3_t0_ENC0M}`
