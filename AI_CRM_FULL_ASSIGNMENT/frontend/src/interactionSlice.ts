
import { createSlice } from '@reduxjs/toolkit'

const slice = createSlice({
  name: 'interaction',
  initialState: {},
  reducers: {
    setInteraction: (_, action) => action.payload
  }
})

export const { setInteraction } = slice.actions
export default slice.reducer
