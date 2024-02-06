import drawBot as db
import random

# Settings
fontName = "Danfo"  # Replace with the name of your variable font
textString = "DANFO AFROTYPE"
fixedFontSize = 400
ELSHMin = 0
ELSHMax = 100
animationDuration = 2  # Duration in seconds
framesPerSecond = 12
totalFrames = animationDuration * framesPerSecond
backgroundColor = (0, 0, 0)  # Black background
pageWidth, pageHeight = 4096, 2048

# Function to interpolate between min and max opsz values
def interpolate(a, b, t):
    return a + (b - a) * t

# Function to generate a random color
def randomColor():
    return (random.random(), random.random(), random.random(), 1)

# Create each frame
for frame in range(totalFrames):
    # Calculate the progress and corresponding opsz value
    t = frame / (totalFrames - 1)
    currentELSH = interpolate(ELSHMin, ELSHMax, t)

    # Set up the page
    db.newPage(pageWidth, pageHeight)
    db.fill(*backgroundColor)
    db.rect(0, 0, db.width(), db.height())

    # Set font and font variations
    db.font(fontName, fixedFontSize)
    db.fontVariations(ELSH=currentELSH)

    # Calculate the total width of the text
    totalTextWidth = sum(db.textSize(letter)[0] for letter in textString)

    # Initial position (start drawing from the center)
    x = (pageWidth - totalTextWidth) / 2
    y = (pageHeight - fixedFontSize) / 2

    # Draw each letter with unique transformation
    for letter in textString:
        # Random transformation parameters
        offsetX = random.uniform(-20, 20) * (currentELSH / ELSHMax)
        offsetY = random.uniform(-20, 20) * (currentELSH / ELSHMax)
        angle = random.uniform(-10, 10) * (currentELSH / ELSHMax)
        scale = 1 + random.uniform(-0.1, 0.1) * (currentELSH / ELSHMax)
        color = randomColor()

        # Apply transformation and draw the letter
        db.save()
        db.translate(x + offsetX, y + offsetY)
        db.rotate(angle)
        db.scale(scale)
        db.fill(*color)
        db.text(letter, (0, 0), align="center")
        db.restore()

        # Update x position for the next letter
        x += db.textSize(letter)[0]

# Save the animation
db.saveImage("~/Desktop/test .mp4", imageResolution=144)
