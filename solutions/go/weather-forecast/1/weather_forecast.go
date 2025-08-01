// Package weather returns the weather forecast for a given location.
package weather

// CurrentCondition contains the value of current weather condition for the location.
var CurrentCondition string

// CurrentLocation contains the location for which forecast is being made.
var CurrentLocation string

// Forecast takes in the city where the forecast is being made , and the condition which denotes the current weather condition over there.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
