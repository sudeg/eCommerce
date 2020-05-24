var process = $(".process");
var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");

var SECTION_WIDTH = 200;

var sections = [];
var create = function (start) {
    var section = {
        start: start,
        width: SECTION_WIDTH,
        height: 45,
        hMax: 35,
        hMod: 0,
        progress: 0,
        dot: {
            x: 0,
            y: 0
        }
    };
    section.end = section.start + section.width;
    section.dot.x = section.start + section.width / 2;
    section.dot.y = section.height;
    sections.push(section);
};

var draw = function (s) {
    var wMod = s.width * 0.3;
    ctx.beginPath();
    ctx.moveTo(s.start, s.height);
    ctx.bezierCurveTo(
        s.start + wMod,
        s.height,
        s.start + wMod,
        s.height - s.hMod,
        s.start + s.width / 2,
        s.height - s.hMod
    );
    ctx.bezierCurveTo(
        s.end - wMod,
        s.height - s.hMod,
        s.end - wMod,
        s.height,
        s.end,
        s.height
    );
    ctx.lineWidth = 4;
    ctx.strokeStyle = "white";
    ctx.stroke();

    ctx.beginPath();
    ctx.fillStyle = "white";
    ctx.arc(s.dot.x, s.dot.y, 8, 0, Math.PI * 2);
    ctx.fill();
};

function quad(progress) {
    return Math.pow(progress, 2);
}

function makeEaseOut(delta) {
    return function (progress) {
        return 1 - delta(1 - progress);
    };
}
var quadOut = makeEaseOut(quad);

var bend = function (s) {
    if (s.progress < s.hMax) {
        var delta = quadOut(s.progress / s.hMax);
        s.hMod = s.hMax * delta;
        s.dot.y = s.height - s.hMax * delta;
        s.progress++;
    }
};
var reset = function (s) {
    if (s.progress > 0) {
        var delta = quadOut(s.progress / s.hMax);
        s.hMod = s.hMax * delta;
        s.dot.y = s.height - s.hMax * delta;
        s.progress -= 2;
    } else {
        s.hMod = 0;
        s.dot.y = s.height;
        s.progress = 0;
    }
};

var currentSection = 0;
process.on("mousemove", function (event) {
    var section = Math.floor(
        (event.clientX - process.offset().left) / SECTION_WIDTH
    );
    currentSection = section;
    process.find(".active").removeClass("active");
    process.find("li").eq(section).addClass("active");
});

create(0);
create(200);
create(400);
create(600);

var loop = function () {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    sections.forEach(function (s, index) {
        if (currentSection === index) {
            bend(s);
        } else {
            reset(s);
        }
        draw(s);
    });

    window.requestAnimationFrame(loop);
};
loop();