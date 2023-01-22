from toga_cocoa.libs import (
    NSImage,
    NSImageAlignment,
    NSImageFrameNone,
    NSImageScaleProportionallyUpOrDown,
    NSImageView,
    NSSize,
)

from .base import Widget


class ImageView(Widget):
    def create(self):
        self.native = NSImageView.alloc().init()

        # self._impl.imageFrameStyle = NSImageFrameGrayBezel
        self.native.imageFrameStyle = NSImageFrameNone
        self.native.imageAlignment = NSImageAlignment.Center.value
        self.native.imageScaling = NSImageScaleProportionallyUpOrDown

        # Add the layout constraints
        self.add_constraints()

    def set_image(self, image):
        if image:
            self.native.image = self.interface._image._impl.native
        else:
            width = self.interface.style.width or 0
            height = self.interface.style.height or 0
            self.native.image = NSImage.alloc().initWithSize(NSSize(width, height))

    def rehint(self):
        pass
