/* pasuspender -- chuck.alsa dummy.ck*/

// impulse to filter to dac
Impulse i => BiQuad f => dac;
// set the filter's pole radius
.99 => f.prad;
// set equal gain zero's
1 => f.eqzs;
// initialize float variable
0.0 => float v;

// infinite time-loop
while( true )
{
    // set the current sample/impulse
    1.0 => i.next;
    // sweep the filter resonant frequency
    Std.fabs(Math.sin(v))*4000 => f.pfreq;
    Std.fabs(Math.sin(v*2))/5 => f.gain;
    // increment v
    v + .1 => v;
    // advance time
    20::ms => now;
}