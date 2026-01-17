export interface CreativeAsset {
  id: string;
  url: string;
  type: 'image' | 'video' | 'layout';
  status: 'uploading' | 'analyzing' | 'completed';
  aiMetadata?: {
    tags: string[];
    style: string;
    scores: {
      technical: number;
      commercial: number;
      innovation: number;
    };
  };
}

export interface PortfolioState {
  title: string;
  assets: CreativeAsset[];
  isGeneratingPitch: boolean;
}