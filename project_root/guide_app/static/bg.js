function Particles(){
  this.colors = [
    '255, 255, 255',
    '255, 99, 71',
    '19, 19, 19'
  ]
  this.blurry = true;
  this.border = false;
  this.minRadius = 10; 
  this.maxRadius = 35;
  this.minOpacity = .005;
  this.maxOpacity = .5;
  this.minSpeed = .05;
  this.maxSpeed = .5;
  this.numParticles = 75;

  this.canvas = document.getElementById('canvas');
  this.ctx = this.canvas.getContext('2d');
  this.particles = [];
}

Particles.prototype.init = function(){
  this.render();
  this.createCircle();
  this.animate();
}

Particles.prototype._rand = function(min, max){
  return Math.random() * (max - min) + min;
}

Particles.prototype.render = function(){
  this.canvas.width = window.innerWidth;
  this.canvas.height = window.innerHeight;

  window.addEventListener('resize', function(){
    this.canvas.width = window.innerWidth;
    this.canvas.height = window.innerHeight;
  });
}

Particles.prototype.createCircle = function(){
  for (let i = 0; i < this.numParticles; i++) {
    let color = this.colors[~~(this._rand(0, this.colors.length))];
    
    this.particles.push({
      radius    : this._rand(this.minRadius, this.maxRadius),
      xPos      : this._rand(0, this.canvas.width),
      yPos      : this._rand(0, this.canvas.height),
      xVelocity : this._rand(this.minSpeed, this.maxSpeed),
      yVelocity : this._rand(this.minSpeed, this.maxSpeed),
      color     : 'rgba(' + color + ',' + this._rand(this.minOpacity, this.maxOpacity) + ')'
    });
  }
}

Particles.prototype.draw = function(p){
  let ctx = this.ctx;
  
  if (this.blurry === true ) {
    let grd = ctx.createRadialGradient(
      p.xPos, p.yPos, p.radius,
      p.xPos, p.yPos, p.radius/1.25
    );
    grd.addColorStop(1.000, p.color);
    grd.addColorStop(0.000, 'rgba(34, 34, 34, 0)');
    ctx.fillStyle = grd;
  } else {
    ctx.fillStyle = p.color; 
  }
  
  if (this.border === true) {
    ctx.strokeStyle = '#fff';
    ctx.stroke();
  }
  
  ctx.beginPath();
  ctx.arc(p.xPos, p.yPos, p.radius, 0, 2 * Math.PI, false);
  ctx.fill();
}

Particles.prototype.animate = function(){
  let self = this;
  
  function loop(){
    self.clearCanvas();
    for (let i = 0; i < self.particles.length; i++) {
      let p = self.particles[i];
      p.xPos += p.xVelocity;
      p.yPos -= p.yVelocity;
     
      if (p.xPos > self.canvas.width + p.radius || p.yPos > self.canvas.height + p.radius) {
        self.resetParticle(p);
      }
      self.draw(p);
    }  
    requestAnimationFrame(loop);
  }
  
  requestAnimationFrame(loop);
}

Particles.prototype.resetParticle = function(p){
  if (this._rand(0, 1) > .5) { 
    p.xPos = -p.radius;
    p.yPos = this._rand(0, this.canvas.height);
  } else {
    p.xPos = this._rand(0, this.canvas.width);
    p.yPos = this.canvas.height + p.radius;   
  }
}

Particles.prototype.clearCanvas = function(){
  this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
}

let particle = new Particles().init();
