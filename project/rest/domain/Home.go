package domain

import (
	"fmt"
	"io/ioutil"
	"net/http"
)

// HOME - Hospitals

/*
start_lat
start_lon
start_name
end_lat
end_lon
end_name
 */

type HomeHospitals []Home

type Home struct {

	StartLat float64 `json:"start_lat" bson:"start_lat"`
	StartLon float64 `json:"start_lon" bson:"start_lon"`
	StartName string `json:"start_name" bson:"start_name"`
	EndLat float64 `json:"end_lat" bson:"end_lat"`
	EndLon float64 `json:"end_lon" bson:"end_lon"`
	EndName string `json:"end_name" bson:"end_name"`

}

func (h Home) GetData() string {
	file, err := ioutil.ReadFile("./data/SortedElPaso.json")
	if err != nil {
		return ""
	}
	rest := string([]byte(file))
	return rest
}

func (h Home) ServeData(w http.ResponseWriter, r *http.Request){
	w.Header().Set("Access-Control-Allow-Origin", "*")

	w.Header().Set("Access-Control-Allow-Headers", "Content-Type")

	fmt.Fprintln(w,Home{}.GetData())
}
