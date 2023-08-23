import QtQuick 2.0
import QtQuick.Window 2.2
import QtQuick.Controls 2.15
Window {
    visible: true
    width: 800
    height: 480

    Rectangle {
        id: main
	    width: 800
	    height: 480
	    anchors.centerIn: parent
	    color: "black"

	    Rectangle {
            id: nav
	        anchors.fill: parent
	        color: "#101010"
	        radius: 40.0
	        border.width: 0

            Item {
                id : clock

                property int hours
                property int minutes
                property int seconds
                property real shift
                property bool night: false
                property bool internationalTime: false //Unset for local time

                function timeChanged() {
                    var date = new Date;
                    hours = internationalTime ? date.getUTCHours() + Math.floor(clock.shift) : date.getHours()
                    night = ( hours < 7 || hours > 19 )
                    minutes = internationalTime ? date.getUTCMinutes() + ((clock.shift % 1) * 60) : date.getMinutes()
                    seconds = date.getUTCSeconds();
                }

                anchors.horizontalCenter : parent.horizontalCenter
                anchors.top: parent.top
                height: time.height
                width: time.width

                Timer {
                    interval: 500; running: true; repeat: true;
                    onTriggered: clock.timeChanged()
                }

                Label {
	                id: time
	                anchors.centerIn: parent
                    color: "white"

	                text: ('0'+clock.hours).slice(-2)+":"+('0'+clock.minutes).slice(-2)
	                font.pixelSize: 250
                }
            }

        }
    }
}
