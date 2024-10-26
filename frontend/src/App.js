import { useEffect } from "react"
import { useQueryParams } from "./useQueryParams"
import { useThreeAppActions } from "./context"

const App = () => {

  const threeAppActions = useThreeAppActions()
  const queryParams = useQueryParams()

  useEffect(() => {
    if (queryParams.has("cubeSize")) {
      threeAppActions.setCubeSize(queryParams.getNumber("cubeSize"))
    }
    if (queryParams.has("animationSpeed")) {
      threeAppActions.setAnimationSpeed(queryParams.getNumber("animationSpeed"))
    }
    if (queryParams.has("autoRotate")) {
      threeAppActions.setAutoRotate(queryParams.getBool("autoRotate"))
    }
    if (queryParams.has("autoRotateSpeed")) {
      threeAppActions.setAutoRotateSpeed(queryParams.getNumber("autoRotateSpeed"))
    }
    if (queryParams.has("axesEnabled")) {
      threeAppActions.setAxesEnabled(queryParams.getBool("axesEnabled"))
    }
  }, [threeAppActions, queryParams])

  return (
    <>
    </>
  )
}

export default App
