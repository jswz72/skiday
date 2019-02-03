(ns skiday.core
  (:require [ajax.core :refer [GET POST]]))

(def app-server "http://localhost:5000")

(defn error-handler [{:keys [status status-text]}]
  (.error js/console status)
  (.error js/console status-text))

(defn handler [{:keys [conditions]}]
  (.log js/console conditions))

(defn get-resort-data [resort]
  (GET (str app-server "/resort/" resort)
     {:handler handler
      :error-handler error-handler
      :response-format :json
      :keywords? true}))

(get-resort-data "cannon")
